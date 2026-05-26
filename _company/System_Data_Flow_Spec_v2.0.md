# ⚙️ D.AAL DESIGN 시스템 데이터 흐름 최종 사양서 (v2.0)
## [목적]
본 문서는 결제(Payment) 및 뉴스레터 구독 관리 시스템의 백엔드 로직 프로토타입 구현을 위한 **운영 계약서** 역할을 합니다. 모든 에이전트와 개발팀은 이 명세를 기준으로 데이터 구조를 확정하고, 오류 처리 시나리오까지 통합 검증해야 합니다.

## [핵심 전제]
1.  모든 비즈니스 액션은 Webhook을 통해 백엔드로 유입됩니다. (Polling 금지)
2.  데이터의 궁극적 목적은 **고객별 성장 이력(Growth History)** 기록 및 KPI 대시보드 연동입니다.

---
## 1. 결제 시스템 웹훅 명세 (Payment Webhook Specification)

결제 게이트웨이(PG사/Stripe 등)로부터 다음 상태 변화 발생 시 반드시 알림을 받아야 합니다.

| 이벤트 이름 (Trigger) | 전송 시점 (Event Timing) | 필수로 수신해야 할 데이터 Payload | 비즈니스 처리 로직 (Action Required) | 오류 대응 및 시스템 반응 (Error Handling) |
| :--- | :--- | :--- | :--- | :--- |
| **`payment.created`** | 고객이 결제를 요청한 직후 | `user_id`, `transaction_id`, `requested_plan_id`, `amount`, `currency`, `timestamp` | 1. 트랜잭션 상태를 'PENDING'으로 기록한다. <br> 2. 사용자에게 임시 성공 메시지를 보여주고, PG사 응답을 기다리게 한다. | **[비고]** 이 시점의 오류는 전송 실패가 아닌 '결제 게이트웨이 통신 문제'로 간주하고 재요청 로직을 설계한다. |
| **`payment.success`** | 결제가 성공적으로 완료된 시점 | `user_id`, `transaction_id`, `final_plan_id`, `amount`, `status: SUCCESS`, `timestamp` | 1. 사용자 계정의 구독 상태를 'ACTIVE'로 업데이트한다. <br> 2. **[Critical]** 해당 Plan에 맞는 기능(예: Standard Tier = 대시보드 접근 권한)을 부여하고, 초기 온보딩 프로세스를 트리거한다. | `status != SUCCESS`일 경우: 실패 처리 로직(`payment_failed`)으로 이관. |
| **`payment.failure`** | 결제에 실패하여 취소된 시점 | `user_id`, `transaction_id`, `requested_plan_id`, `reason_code`, `message` | 1. 사용자 계정의 구독 상태를 'PAUSED' 또는 'EXPIRED'로 변경한다. <br> 2. 시스템은 실패 사유(예: 카드 만료)에 맞는 **개선 가이드 및 재결제 유도 메시지**를 생성하여 전송해야 한다. | `reason_code`가 명확하지 않을 경우: 사용자에게 일반적인 오류 메시지를 제공하고, 관리자 알림을 발송한다. |
| **`subscription.canceled`** | 사용자가 구독 취소 버튼 클릭 시 | `user_id`, `current_plan_id`, `cancellation_reason` (선택), `effective_end_date` | 1. 계정 상태를 'PENDING_CANCELLATION'으로 변경한다. <br> 2. **[Retention Logic]** 취소 시점을 기준으로 N일 전(예: 7일)에 재활성화 유도 알림을 발송할 로직이 작동해야 한다. | - |

---
## 2. 뉴스레터 구독 관리 시스템 웹훅 명세 (Newsletter Webhook Specification)

뉴스레터는 단순한 마케팅 채널이 아닌, **'잠재 고객 리드(Lead)'의 상태 변화**를 추적하는 핵심 데이터입니다.

| 이벤트 이름 (Trigger) | 전송 시점 (Event Timing) | 필수로 수신해야 할 데이터 Payload | 비즈니스 처리 로직 (Action Required) | 오류 대응 및 시스템 반응 (Error Handling) |
| :--- | :--- | :--- | :--- | :--- |
| **`subscription.subscribed`** | 사용자가 뉴스레터 구독 폼 제출 시 | `user_id`, `email`, `timestamp`, `source` (유입 경로: Landing Page/Paid Ad 등) | 1. DB에 새로운 리드(Lead)를 등록하고, 기본 점수(Score=10점)를 부여한다. <br> 2. 유입 경로(`source`) 데이터를 기반으로 잠재 고객 그룹을 분류한다. | 중복 이메일 주소: 이미 구독자가 존재하는지 확인 후, 기존 기록만 업데이트하고 경고 로그를 남긴다. |
| **`subscription.unsubscribed`** | 사용자가 뉴스레터 수신 거부 시 | `user_id`, `email`, `timestamp` | 1. DB에서 해당 이메일을 'Unsubscribed' 상태로 플래그 처리한다. <br> 2. CRM/마케팅 자동화 시스템에 알림을 보내서 마케팅 활동 중단을 지시한다. | - |

---
## [현빈의 전략적 코멘트]

**[비고]** 위 명세에서 가장 중요한 것은 **'상태 전이(State Transition)'**를 추적하는 것입니다. 단순한 '성공/실패' 기록을 넘어, 고객이 `PENDING` $\to$ `ACTIVE` $\to$ `PAUSED` $\to$ `CANCELED` 와 같은 상태 변화를 겪을 때마다 이 로직들이 작동해야만 **데이터 기반의 예측 모델링**이 가능합니다. 개발팀은 트랜잭션 ID와 사용자 ID를 기준으로 모든 상태 변경 히스토리를 저장하는 스키마 설계에 집중해 주십시오.