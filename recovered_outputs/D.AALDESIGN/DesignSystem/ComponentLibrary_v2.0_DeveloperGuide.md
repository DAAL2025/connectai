# 🛠️ D.AAL DESIGN Component Library v2.0: 리스크 기반 운영 시스템 (Developer Guide)
## 🎯 목표
Mini-Audit Funnel의 모든 컴포넌트가 Researcher가 제시한 **'재무적 손실 비용($FC$)'** 데이터를 핵심 변수로 사용하도록 설계한다. 단순한 UI를 넘어, 데이터에 반응하는 '운영 시스템 인터페이스'로 구현되어야 한다.

---

## 🎨 1. 시스템 색상 팔레트 및 스케일링 가이드라인
| 용도 (Use Case) | 색상명/개념 | HEX Code | SCALING/변수 바인딩 지침 |
| :--- | :--- | :--- | :--- |
| **Primary BG** (배경) | Deep Navy / System Base | `#0A1931` | 모든 핵심 콘텐츠의 배경색. '안정성'과 '전문성'을 부여하며, 데이터 흐름 시각화에 사용됨. |
| **Accent 1** (수익/성장) | Coral Orange / MRR Flow | `#FF6B3D` | **[Data Binding]** 모든 수익 관련 수치(MRR, 예상 매출), 성장 화살표, CTA 강조색. '돈'과 직결됨을 시각적으로 각인. |
| **Accent 2** (경고/위험) | Amber Warning / $FC$ Alert | `#FFC107` | **[Data Binding]** 초기 진단 단계의 위험 감지, 경고 게이지의 '주의' 구간에 사용. 시스템 문제 발생 시 즉각적 주의 유발. |
| **Accent 3** (심각/위기) | Crimson Red / Critical Failure | `#DC3545` | **[Data Binding]** $FC$가 임계치(Threshold)를 초과했을 때의 경고, 결제 실패 시뮬레이션 등 '즉시 개입 필요' 지점에만 사용. |
| **Text/Foreground** | Off-White Text | `#E0F7FA` | Deep Navy 배경 위 텍스트 기본 색상. 가독성 최우선. |

---

## 📈 2. 핵심 컴포넌트: Failure Cost (FC) Risk Gauge
이 게이지는 Mini-Audit Funnel의 첫 화면에 위치하며, 사용자의 비즈니스 리스크를 즉각적으로 시각화하는 역할을 합니다.

**[개발자 바인딩 지점]**
*   **Input Variable:** `failure_cost_amount` (Number: 월간 예상 손실 금액)
*   **Secondary Input:** `risk_percentage` (Number: 0.0 to 1.0, 리스크 비율)

**[구조 및 동작 로직]**
1.  **Gauge Container:** 전체 너비 $100\%$를 차지하는 원형 또는 바 형태의 게이지 컴포넌트.
2.  **Fill Logic (핵심):** `risk_percentage`에 따라 채워지는 영역의 길이가 결정됨.
3.  **Color Mapping Logic:**
    *   $0\% \sim 40\%$ : `#E0F7FA` (Green/Safe) $\to$ '안정적' 메시지 출력.
    *   $40\% \sim 85\%$ : `Amber Warning (#FFC107)` $\to$ '주의 필요' 경고 아이콘(⚠️) + $FC$ 제시.
    *   $85\% \sim 100\%$ : `Crimson Red (#DC3545)` $\to$ **"Critical Failure Detected."** 즉각적인 문제 해결 솔루션 CTA로 유도.

**[예시 구현 (Pseudo-Code)]**
```javascript
const calculateRiskLevel(cost) {
    if (cost > 3000000) return { color: '#DC3545', message: 'Critical Risk' }; // $3M 초과 시 빨간색
    if (cost > 1000000) return { color: '#FFC107', message: 'High Alert' }; // $1M 초과 시 주황색
    return { color: '#4CAF50', message: 'Stable' };
}

// renderGauge(failure_cost_amount): 
//   const risk = calculateRiskLevel(failure_cost_amount);
//   <div style={{ background: risk.color, width: `${risk.percentage}%` }}></div>;
```

---

## 📊 3. 핵심 컴포넌트: Growth Tier Comparison Table (비교표)
단순한 '기능 비교'가 아닌, **'리스크 관리 및 안정성 확보 능력'**을 기준으로 상품들을 비교합니다.

**[개발자 바인딩 지점]**
*   각 기능 셀은 단순 텍스트가 아닌, `is_feature_available` (Boolean)와 `impact_reduction_rate` (Number: %)를 받아야 합니다.

| Feature Group | Basic Plan | Growth Engine Retainer (⭐ 권장) | Enterprise System |
| :--- | :--- | :--- | :--- |
| **데이터 흐름 안정성** | 기본 API 연결 (Limited Scope) | ✅ **24/7 실시간 $FC$ 모니터링 시스템** (`[근거: Researcher No.1]`) | ✅ 전용 서버, 무제한 트래픽 및 커스텀 리스크 로직 |
| **리스크 시뮬레이션** | ❌ (수동 계산) | ✅ **Mini-Audit Live Simulation** (자동 $FC$ 예측 게이지 탑재) (`[근거: Mini-Audit]`) | ✅ 전담 컨설턴트 기반의 주간 리스크 워크숍 포함 |
| **성장 로직 설계** | 단순 웹사이트 제작 | ✨ **MRR 기반 Growth Logic 매핑** (반복 매출 구조화) (`[근거: Self-RAG]`) | ✨ 시스템 레벨 최적화, 비즈니스 모델 재설계 |
| **가격/CTA** | $X$만원 / Trial Start | $\mathbf{Y}$만원 / **Secure System Now** (CTA 강조색 사용) | 견적 문의 / Custom Proposal |

---

## 🧠 4. 종합 디자인 흐름(Wireframe Flow Logic)
1.  **[Landing Page]**: 히어로 영역에서 "단순한 웹사이트 제작을 넘어, 성과를 측정하는 비즈니스 운영 시스템을 구축합니다." (Self-RAG H1) 제시.
2.  **[Pain Point/Audit Start]**: Researcher의 데이터를 활용하여 '당신의 현재는 어느 정도 손실되고 있습니까?' 질문 던지기. $\to$ **FC Risk Gauge 컴포넌트가 작동하며 $FC$를 시각화.** (위기감 조성).
3.  **[Solution/Comparison]**: 위기를 인지한 사용자에게 가장 현실적인 대안 제시. $\to$ **Growth Tier Comparison Table을 통해, '성장 로직'과 '운영 시스템 안정성'이 필수임을 강조.**
4.  **[CTA]**: Mini-Audit 페이지로 유도하며, "시스템 감사를 받아보세요" CTA를 배치.

***End of Component Library v2.0***