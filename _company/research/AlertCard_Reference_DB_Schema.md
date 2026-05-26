# 📊 Alert Card 레퍼런스 데이터베이스 스키마 설계 (v1.0)`

```markdown
## 목표: 'Alert Card System'의 기능적, 비즈니스적 성공 사례를 구조화하여 수집한다.

### I. 핵심 목적 및 활용 가치
이 DB는 단순히 디자인 참고 자료가 아닙니다. 각 레퍼런스가 어떤 **Pain Point**을 해결하고, 어떠한 **비즈니스 데이터(KPI/Metric)**와 연결되어 최종적으로 고객의 **어떤 액션(Action Step)**을 유도하는지 분석하여, 우리 서비스의 핵심 가치 제안서(Value Proposition)를 강화하는 근거 자료가 됩니다.

### II. DB 구조 (Schema Definition)
각 레퍼런스 항목은 다음 7가지 필드를 반드시 포함해야 합니다.

| 필드명 | 데이터 타입 | 필수 여부 | 설명 및 수집 목표 | 연관 기능/의미 |
| :--- | :--- | :--- | :--- | :--- |
| **1. Reference ID** | String (Unique) | O | 레퍼런스를 식별할 고유 ID (e.g., AC_001) | 관리용 |
| **2. Source URL/Screenshot** | Link/Image | O | 실제 레퍼런스 출처 링크 및 캡쳐 이미지 | 시각적 근거 |
| **3. 핵심 비즈니스 목표** | Text | O | 이 카드가 해결하려는 궁극적인 비즈니스 문제 (Pain Point) 정의. (예: 구매 전환율 하락, 사용자 이탈 직전 감지 등) | 🎯 Pain Point 연결 |
| **4. 데이터 소스 및 트리거** | Multi-select | O | 이 경고가 발생하게 만든 근본 데이터의 종류와 조건. (e.g., GA 데이터 - 장바구니 이탈, CRM 데이터 - 마지막 접속일 > 30일) | 📊 입력값 정의 |
| **5. 알림 유형 및 심각도** | Enum | O | 경고/알림의 분류와 시각적 중요도 (Critical, Warning, Info). 오렌지 코랄 등의 색상 기준 확립 근거 확보. | 🚨 Severity & State |
| **6. 제시된 액션 스텝 (Action Step)** | Text | O | 사용자에게 실제로 취하도록 유도하는 구체적인 행동 지침. ("지금 상품 재고를 확인하세요", "친구에게 공유하여 할인 쿠폰 받기") | ✅ Call to Action (CTA) |
| **7. D.AAL 적용 가능성 및 개선점** | Text | O | 이 레퍼런스를 우리 서비스에 도입할 때의 장점, 그리고 우리의 시스템 아키텍처를 고려한 구체적인 개선 제안. | 💡 인사이트 추출 |

### III. 리서치 실행 원칙 (Researcher's Guide)
1. **수집 방향:** 단순히 '예쁜 디자인'을 찾는 것이 아니라, **"왜 이 카드가 여기에 표시되었는가?"**에 대한 답변을 얻는 데 집중합니다.
2. **검색 키워드 예시:** `[industry] + predictive alert system`, `dashboard widget [metric] anomaly detection`, `SaaS user retention warning card UI` 등 비즈니스 언어 기반으로 검색합니다.
3. **분류 기준 (우선순위):** ① 데이터 소스의 명확성 $\rightarrow$ ② 액션 스텝의 구체성 $\rightarrow$ ③ 심각도에 따른 시각적 계층 구조를 순서로 검토하며 레퍼런스를 수집합니다.