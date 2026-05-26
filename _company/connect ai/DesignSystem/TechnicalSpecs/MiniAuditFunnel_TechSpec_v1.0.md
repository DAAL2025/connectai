# 🛠️ Mini-Audit Funnel: Critical Alert Module (CAM) 및 전체 컴포넌트 기술 사양서 (V1.0)

**작성 목적:** D.AAL DESIGN의 핵심 서비스인 '재무적 손실 비용($FC$) 시뮬레이션' 페이지를 개발자가 즉시 구현할 수 있는 완벽한 스펙 문서 제공.
**대상 아티스트/개발자:** 프론트엔드(React/Next.js), 백엔드(FastAPI/Pydantic) 엔지니어.

---

## 1. 🚨 Critical Alert Module (CAM) 상세 사양서

CAM은 단순한 데이터 표시가 아닌, 재무적 위기감을 시각화하는 인터랙티브 컴포넌트입니다. 이 모듈의 핵심은 $FC$ 수치의 **변화에 따른 사용자 심리 자극(Urgency)**입니다.

### 1.1. 애니메이션 및 상호작용 스펙 (CSS/JS)
| 항목 | 기술 스펙 | 설명 |
| :--- | :--- | :--- |
| **데이터 바인딩** | `onDataLoaded(fcValue, riskLevel)` 함수 호출 필수 | 백엔드 API 응답을 받은 즉시 이 함수를 실행하여 게이지와 텍스트를 업데이트합니다. |
| **게이지 변화 (CSS)** | CSS Transition: `width`, `background-color` 속성 사용. `transition: width 1.5s ease-out, background-color 0.8s linear;` 적용. | 수치가 바뀔 때 부드럽지만 즉각적인 느낌을 주도록 애니메이션합니다. |
| **위기 레벨 색상 (CSS)** | **Low Risk:** `#4CAF50` $\rightarrow$ **Medium Risk:** `#FFC107` $\rightarrow$ **High/Critical Risk:** `#D32F2F` (강한 빨간색) | $FC$ 값의 변화율(Rate of Change)과 절대값에 따라 색상을 결정합니다. |
| **애니메이션 로직 (JS)** | 1. 초기화 시 게이지를 0%로 설정하고, `requestAnimationFrame`을 사용하여 최종 `$FC$` 비율까지 부드럽게 채워나갑니다. <br>2. $FC$가 임계치(Threshold)에 도달할 때마다 **강한 깜빡임 효과(Pulsating Animation)** 또는 경고 아이콘의 크기 변화를 추가합니다. |
| **핵심 반응** | `$FC$` 값이 1시간 단위로 시뮬레이션되는 경우, 게이지 바와 숫자가 *'현재 시간 대비 얼마나 빠르게 손실되고 있는지'*를 보여주며 역동적으로 움직여야 합니다. |

### 1.2. 데이터 바인딩 및 API 스펙
**[API Endpoint]**: `/api/v1/mini-audit/fc-simulation` (POST)
**[요청 데이터 구조 (Request Body)]**:
```json
{
  "business_name": "string", // 사용자 입력
  "industry_type": "string", // 사용자 선택 (예: E-commerce, SaaS 등)
  "operational_data_inputs": {
    "monthly_revenue_estimate": 15000, // 예상 월 매출 (USD)
    "current_tech_debt_score": 7.5,  // 현재 기술 부채 점수 (1-10점)
    "system_efficiency_rate": 0.65   // 시스템 효율성 비율 (0.0 - 1.0)
  }
}
```

**[응답 데이터 구조 (Response Body)]**:
```json
{
  "status": "success",
  "data": {
    "calculated_fc_value": 4520.75, // 최종 계산된 재무 손실 비용 (USD) - 소수점 둘째 자리까지
    "risk_level": "Critical",      // Risk Level: Low/Medium/High/Critical
    "explanation_key": "tech_debt_systemic_failure", // 이 FC가 발생한 근본적인 원인 코드
    "suggested_action": "Mini-Audit Funnel 페이지의 CTA를 트리거할 메시지 키"
  }
}
```

---

## 2. ✨ Mini-Audit Funnel 컴포넌트 명세서 (Full Funnel Specification)

Funnel은 위기감 조성 $\to$ 솔루션 제시 $\to$ 구매 유도로 이어지는 **5개의 핵심 섹션**으로 구성됩니다. 각 섹션별로 재사용 가능한 UI 컴포넌트를 정의합니다.

### 2.1. Section A: Hero - Failure Hook (문제 인식 극대화)
*   **목표:** 사용자가 현재의 문제를 '개선'이 아닌, '재무적 위기(Failure)'로 인지하게 만듭니다.
*   **컴포넌트:** `Hero_DynamicDataFlow`
    *   **스펙:** 배경에 미세한 데이터 흐름(Data Flow) 애니메이션을 지속적으로 재생합니다 (Static $\to$ Dynamic).
    *   **핵심 요소:** H1/H2 텍스트는 정적이지만, CTA 버튼 근처에는 작은 **'MRR 예측 시뮬레이터' 위젯**이 상시 활성화되어 있어 '측정 가능성'을 강조해야 합니다.

### 2.2. Section B: Pain Point - The Gap (기존 방식의 문제 제기)
*   **목표:** 기존 웹사이트 제작 방식을 '미완성 시스템(Under-engineered System)'으로 규정합니다.
*   **컴포넌트:** `Comparison_GlitchEffectCard`
    *   **스펙:** 일반적인 웹사이트와 D.AAL DESIGN의 접근법을 비교하는 카드 UI를 사용하되, 기존 방식의 설명은 **깨진 폰트/회색/글리치(Glitch) 효과**를 적용하여 불안정함을 시각화합니다.
    *   **데이터 바인딩:** '기술 부채'와 관련된 통계 자료는 근거 출처(예: `[근거: 업계 평균 대비 X% 부족]`)가 명확하게 표시되어야 합니다.

### 2.3. Section C: Solution - Growth Logic (D.AAL의 시스템 제시)
*   **목표:** D.AAL DESIGN의 접근법이 '디자인'이 아니라 '시스템 설계'임을 증명합니다.
*   **컴포넌트:** `Growth_ProcessFlowDiagram`
    *   **스펙:** 3단계 프로세스를 보여주는 플로우 다이어그램입니다. 화살표는 **오렌지 코랄(#FF6B3D)** 계열을 사용하여 '데이터의 흐름'과 '돈의 흐름(Flow of Money & Data)'이 연결되어 있음을 시각적으로 강조합니다.
    *   **인터랙션:** 각 단계 설명 텍스트 위에 마우스를 올리면, 해당 로직이 구체적으로 어떤 데이터(예: `MRR`, `CAC`)를 다루는지 토스트 알림으로 표시됩니다.

### 2.4. Section D: Conversion - CAM Display (위기감 최고조)
*   **목표:** 사용자의 위기감을 최대로 끌어올리고, 다음 행동을 강제합니다.
*   **컴포넌트:** `CriticalAlertModule` (Section 1 참조)
    *   **핵심:** 이 섹션에 도달한 사용자에게는 '문제점(Pain Point)'보다 **'즉각적인 재무적 결과($FC$ 수치)'**가 가장 먼저 보여야 합니다.

### 2.5. Section E: Call to Action (행동 유도)
*   **목표:** Funnel의 최종 목표인 Mini-Audit 실행을 유도합니다.
*   **컴포넌트:** `Interactive_MiniAuditForm`
    *   **스펙:** 일반적인 '문의하기' 버튼이 아닌, **"무료 시스템 감사 요청"**이라는 문구를 사용하며, 이 과정이 컨설팅의 시작임을 강조해야 합니다.
    *   **UX:** 양식 제출 전, "지금 $FC$를 확인하고 성장의 기회를 잡으세요."와 같은 재무적 압박을 주는 최종 카피가 배치되어야 합니다.

---

## 📝 구현 우선순위 및 개발 가이드라인 요약

1.  **API 설계 최우선:** `/api/v1/mini-audit/fc-simulation` 엔드포인트의 Pydantic 스키마와 백엔드 유효성 검증 로직을 가장 먼저 확정하고 테스트합니다.
2.  **CAM 구현 우선:** CAM 컴포넌트가 API 응답에 따라 정확히 애니메이션되는지 확인하는 것이 Funnel 구축의 핵심 성공 지표입니다.
3.  **컴포넌트 시스템화:** 모든 섹션별 UI는 `DesignSystem/ComponentLibrary_v2.0` (최근 생성된 파일)을 기반으로 재사용 가능하도록 구성합니다.