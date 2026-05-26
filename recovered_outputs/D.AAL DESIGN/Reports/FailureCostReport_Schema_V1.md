# D.AAL DESIGN 컨설팅 보고서: 데이터 스키마 정의
**목표:** 모든 콘텐츠가 정량화된 '재정적 손실 비용(Failure Cost)'을 중심으로 서술되도록 강제한다.

## 📊 섹션별 필수 포함 항목 (Mandatory Data Fields)

### 1. [진단 보고서] 핵심 KPI 및 요약
*   **[Input Field: Current System Failure Rate]:** 현재 시스템의 문제 비율 (%)
*   **[Input Field: Estimated Annual Loss Cost]:** 추정 연간 손실 비용 (숫자 + 통화 단위)
*   **[Output Metric 1 - Before]:** 개선 전 예상 성과 지표 (예: 월평균 트래픽, 전환율)
*   **[Output Metric 2 - After]:** Growth OS 적용 후 예상 성과 지표 (Growth Factor 반영)

### 2. [진단 보고서] Failure Cost 상세 데이터 시퀀스 (전/후 비교용)
| 측정 항목 (Metric Name) | 단위 (Unit) | Before State Value (데이터) | Failure Cost 계산 (Before $\rightarrow$ Loss) | After State Value (예측치) | Improvement (%) | 근거 자료 출처 (Source Link) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A. 기술 부채 규모** | 만원 | X,XXX | *[자동 계산]* | YYY | Z% | [Writer/Researcher] |
| **B. 결제 이탈률** | % | 25% (데이터) | $X 비용 발생 구조 분석 필요 | <10% 예상 | - | [Writer/Researcher] |
| **C. 리드-고객 전환 주기** | 일(Days) | 60일 | $XXX 시간적 기회비용 손실 | 15일 이하 | - | [Writer/Researcher] |

### 3. [진단 보고서] 액션 플랜 (Action Plan)
*   **[Input Field: Recommended Tier]:** 가장 적합한 Growth Engine Retainer 티어 (Tier 1, 2, or 3).
*   **[Output Value: Estimated Next Investment Cost]:** 다음 투자 단계에 필요한 예상 비용.

---