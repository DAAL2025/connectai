# 🎨 D.AAL DESIGN Growth Engine Pricing Section (Final Handoff Spec)

## 🎯 목표 섹션: 성장 엔진 리테이너 상품 비교 및 선택 유도
**위치:** 웹사이트 메인 페이지, 스크롤 하단부 (CTA 직전)
**핵심 메시지:** "단순한 비용이 아닌, 예측 가능한 성장에 대한 투자입니다."

---

### 1. 컴포넌트 구조 및 레이아웃 명세 (System Kit 기반 적용)
*   **섹션 컨테이너:** `padding: vertical 120px` / `background-color: #FFFFFF` / `max-width: 1440px`
*   **타이포그래피 스케일:** H2는 시스템 키트의 Primary Heading (3rem, Weight 600) 사용. 모든 본문은 System Body Large (1.125rem) 적용.
*   **배경 효과:** 미세한 그리드 패턴을 배경에 적용하여 '시스템' 느낌 유지 (`background-image: linear-gradient(to right, rgba(10, 25, 49, 0.03), transparent);`).

### 2. 핵심 컴포넌트 상세 명세 (Growth Engine Card)
| 요소 | 규격/값 | 스타일 및 애니메이션 스펙 | 근거/비고 |
| :--- | :--- | :--- | :--- |
| **카드 컨테이너** | 가로 폭: 350px / 간격: 24px (Gap) | `border-radius: 12px` / 기본 배경: `#FFFFFF` | 컴포넌트화 완료. |
| **가격(Price)** | 크기: 6rem (Bold) | 색상: 오렌지 코랄 (`#FF6B3D`) / 트랜지션: `transform scale(1.05)` (Hover 시) | 가장 눈에 띄는 CTA의 중심 요소. |
| **서브 타이틀** | 크기: 1.2rem (Medium Weight) | 색상: `#4A4A4A` / 트랜지션: `opacity 0` $\rightarrow$ `opacity 1` (Load 시 Fade In) | "예측 가능한 성장 시스템" 등 가치 설명. |
| **핵심 기능 목록** | 아이콘 + 텍스트 리스트 | 체크 아이콘 색상: `#FF6B3D`. 각 항목은 컴포넌트화된 `FeatureItem` 사용. | 'MRR 예측', '기술 부채 제거' 등의 키워드를 반드시 포함할 것. |
| **CTA 버튼 (Action)** | 크기: 100% / 높이: 56px | 배경색: `#FF6B3D`. 호버 시: `background-color: #e8593b` + 미세한 그림자 효과(Shadow). | "지금 시스템 설계 요청하기" (최종 CTA) |

### 3. 인터랙션 상세 명세 (Interaction Logic - Critical)
*   **[Growth Engine Card] 전체 호버 액션:** 마우스 커서가 카드 영역에 진입하면, 카드가 미묘하게 **Z축으로 떠오르는 듯한(Elevation)** 효과를 주어 사용자에게 집중도를 높입니다. (`transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1)`)
*   **[Simulation Display] - (가장 중요):** 카드 중앙에 위치하는 '월간 수익 예상 시뮬레이터' 영역은 단순 텍스트가 아닌, **실시간으로 변동 가능한 그래프/UI 컴포넌트**로 설계되어야 합니다. 이는 정적인 디자인이 아니라, 상호작용을 유도하는 핵심 요소입니다.
    *   *구현 스펙:* 이 섹션은 별도의 인터랙티브 모듈로 분리하여 개발해야 함.

### 4. 자가 검토 및 다음 단계 지시
**검증 사항:** 모든 색상, 크기, 간격이 `_design_system_kit`의 규격을 따르는지 재확인 필요. 특히 컴포넌트 경계선 처리(Border/Shadow)에 주의할 것.