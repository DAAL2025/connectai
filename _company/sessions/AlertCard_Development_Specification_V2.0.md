# 🚨 Alert Card System 통합 개발 명세서 (v2.0)

**[문서 목적]**
본 문서는 D.AAL DESIGN의 Growth Engine Dashboard에 적용될 'Alert Card System'의 최종 사용자 인터페이스(UI), 인터랙션(UX), 그리고 백엔드 데이터 흐름(API Contract)을 통합하여 개발팀이 별도의 질문 없이 즉시 구현할 수 있도록 하는 **최종 계약서**입니다.

---
## 1. 시스템 개요 및 비즈니스 로직 (Business Logic & Context)
*   **시스템 역할:** 사용자에게 예측 모델(Prediction Engine)의 이상 징후 또는 중요한 액션이 필요함을 즉각적으로 경고합니다. 단순 알림을 넘어, **특정 비즈니스 워크플로우를 촉발**시키는 역할을 수행합니다. [근거: Self-RAG, 현빈 보고서]
*   **핵심 원칙:** Alert Card는 단순히 빨간불이 아닙니다. **"무엇이 문제인지 (What)", "왜 문제가 생겼는지 (Why)", 그리고 "어떻게 해결해야 하는지 (Action Step)"**를 명확히 제시해야 합니다. [근거: Self-RAG]
*   **Alert Level 정의:**
    *   **Critical (심각):** 즉시 액션 필요 (예: 결제 실패, 예상 매출 급락). 색상: **빨강 계열(#D9534F)** / 강조: 🚨 아이콘.
    *   **Warning (주의):** 모니터링 및 계획 필요 (예: 특정 지표 하락 추세). 색상: **주황 계열(#FF6B3D)** / 강조: ⚠️ 아이콘.
    *   **Info (정보):** 참고 및 학습 자료 제공 (예: 새로운 리포트 발행). 색상: **파랑 계열(#0A1931) - Low Contrast** / 강조: ℹ️ 아이콘.

---
## 2. 인터페이스 명세 (UI/UX Mock-up Specification)
*   **(참조 파일):** [AlertCard_DesignSystemSpec_v1.0.md]의 디자인 시스템 컴포넌트와 최종 Figma Mock-up을 따릅니다.
*   **레이아웃 구조:** (반응형 웹 기준, 데스크톱 우선)
    1.  **헤더/제목 영역:** Alert Level에 맞는 엠블럼과 Card Title이 중앙 정렬됩니다. [근거: Self-RAG]
    2.  **핵심 메시지 영역 (Body):** 문제의 원인(Problem Cause)을 간결한 문장으로 제시합니다. 'Pain Point'를 직접적으로 언급하는 카피라이팅 사용 권장. [근거: Writer 비교표]
    3.  **상세 정보 및 시각화:** 발생 지표 그래프 (직전 7일 대비 하락률 등)와 해당 Alert의 *재무적 영향 예상치*를 함께 제시합니다. [근거: Growth Engine, Self-RAG]
    4.  **액션 유도 영역 (CTA):** **가장 중요함.** 문제 해결을 위한 구체적인 액션 버튼 1~3개가 배치됩니다. CTA는 단순 링크가 아닌, 시스템 내 특정 페이지로의 워크플로우 이동 트리거여야 합니다. [근거: Self-RAG]

---
## 3. 데이터 및 API 계약 명세 (Technical Contract Specification)
**[🚨 코다리 에이전트에게 전달할 핵심 요구사항]**
Alert Card를 구동하는 백엔드 API 엔드포인트와 클라이언트 측 TypeScript 인터페이스(Schema)는 아래 구조를 반드시 따라야 합니다.

### 3.1. API Endpoint 정의 (GET /api/v1/alerts)
*   **기능:** 사용자의 계정 및 기간에 기반하여 활성화된 Alert Card 목록을 가져옵니다.
*   **요청 매개변수 (Request Params):** `user_id` (필수), `date_range` (선택, 기본값: 최근 7일).

### 3.2. 응답 스키마 정의 (Response Schema)
```typescript
interface AlertCard {
  alertId: string; // 고유 식별자
  level: 'CRITICAL' | 'WARNING' | 'INFO'; // 필수 값
  title: string; // 사용자가 이해하기 쉬운 핵심 제목
  description: string; // 상세 문제 설명 (Why)
  causeData: { 
    metricName: string; // 어떤 지표가 문제인지 (예: MRR Growth Rate, Conversion Rate)
    currentValue: number; // 현재 값
    threshold: number; // 기준치 또는 목표값
    comparisonMetric?: number; // 비교 지표 (예: 전주 대비 -15%)
  };
  actionStep: { 
    stepName: string; // 액션 단계 이름 (예: '결제 시스템 점검', 'A/B 테스트 재설계') [근거: 현빈 보고서]
    workflowEndpoint: string; // 이 액션을 수행할 내부 페이지 경로 (예: /admin/payment-check)
    suggestedAction?: string; // 사용자가 취해야 할 구체적인 행동 문구 
  };
  createdAt: Date;
}
```

### 3.3. 인터랙션 및 데이터 흐름 시나리오 (Flow Diagram - 개발 검증용)
1. **[초기 로드]**: Dashboard 로드 $\rightarrow$ `/api/v1/alerts?user_id=...` 호출.
2. **[렌더링]**: API 응답 기반으로 Alert Card 컴포넌트를 렌더링. (Level별 색상 및 아이콘 적용)
3. **[클릭 이벤트]**: 사용자가 특정 `AlertCard`의 CTA 버튼 클릭 $\rightarrow$ 해당 Alert가 요구하는 `workflowEndpoint`로 페이지 이동 또는 모달(Modal) 호출.
4. **[데이터 업데이트]**: 액션 수행 후, Dashboard 상단 요약 지표 (KPI)를 재계산하고 시각화하여 즉시 반영되어야 합니다.

---

**[총평 및 다음 단계 결정]**
Alert Card System의 디자인 명세와 데이터 요구사항이 통합되었습니다. 이제 이 사양을 기반으로 **코다리 에이전트가 실제로 구현할 컴포넌트 코드 스켈레톤과 API 엔드포인트 초안**을 작성하여, 비즈니스 로직(현빈)에 의해 검증받는 것이 다음 가장 중요한 단계입니다.