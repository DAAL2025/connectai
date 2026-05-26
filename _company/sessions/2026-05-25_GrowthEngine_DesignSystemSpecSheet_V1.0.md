# 🚀 D.AAL DESIGN Growth Engine Retainer - Design System Specification Sheet V1.0

## 🎯 1. 프로젝트 목표 및 핵심 원칙
*   **목표:** 웹사이트를 단순한 브로슈어가 아닌, **'예측 가능한 비즈니스 운영 시스템'의 인터페이스**로 구현한다.
*   **핵심 컨셉:** Static $\rightarrow$ Dynamic (정적 정보 전달 $\rightarrow$ 동적인 성장 로직 시뮬레이션)
*   **톤 앤 매너:** 전문성(Authority), 기술력(Sophistication), 신뢰(Trust).

## 🎨 2. 디자인 토큰 및 컬러 팔레트 (Design Tokens & Color Palette)
모든 색상은 HEX 코드를 기준으로 하며, 명도 변화를 통해 상태별(State) 사용을 강제합니다.

| 역할 | 이름 | HEX 코드 | 용도 및 규칙 | 근거 |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | Deep Navy | `#0A1931` | 배경, 텍스트 본문 (가장 중요). 전체 구조의 기반. | 자율 사이클 메모리 |
| **Accent/CTA** | Orange Coral | `#FF6B3D` | CTA 버튼, 핵심 그래프 강조, 데이터 플로우 화살표. 행동 유도 지점. | 자율 사이클 메모리 |
| **Secondary** | Light Gray | `#F8FAFC` | 섹션 배경 분리, 카드 배경. Deep Navy와의 대비를 통한 가독성 확보. | 일반적인 웹 디자인 원칙 |
| **Danger/Alert** | Warning Yellow | `#FFC107` | Pain Point 지적, 경고 아이콘(⚠️). 문제 영역 강조. | Writer 비교표 |
| **Success/Flow** | Teal Accent | `#26A69A` | 시스템 작동 완료, 긍정적인 데이터 흐름 시각화. | 자율 사이클 메모리 (데이터 플로우) |

### 🔡 타이포그래피 규격 (Typography Specs)
*   **폰트:** Pretendard (가독성 최우선).
*   **H1 (최대 제목):** 48px, Bold, Deep Navy. (전체 페이지의 가장 강력한 메시지)
*   **H2 (섹션 제목):** 32px, SemiBold, Deep Navy. (시스템 구성 요소 분리)
*   **Body Text:** 16px, Regular, `#4A5568` (딥 네이비보다 약간 밝은 회색으로 장시간 가독성 확보).
*   **CTA Button Text:** 18px, Bold, White.

## 🧩 3. 핵심 컴포넌트 명세서 (Component Atlas)
모든 요소는 반드시 다음의 상태(State)와 상호작용(Interaction)을 갖도록 설계되어야 합니다.

### A. Hero Section Component
*   **기본 구조:** H1 $\rightarrow$ H2 $\rightarrow$ CTA Block $\rightarrow$ Visualizer.
*   **상태 1 (Static):** 초기 로딩 상태. 배경의 데이터 플로우 애니메이션(Data Flow)이 아주 미세하게 움직이는 듯한 효과를 유지한다. (시각적 깊이 부여).
*   **상태 2 (Hover - CTA):** 마우스를 올리면 버튼 색상이 Deep Navy에서 Orange Coral로 순간적으로 전환되며, 아래에 작은 'MRR 예측' 개념의 상승 그래프 아이콘이 따라 움직인다.
*   **필수 인터랙션:** H1 바로 밑에 위치한 서브 문구는 스크롤 시 페이드인(Fade-in)되어야 하며, 배경 데이터 플로우가 텍스트를 통과하는 듯한 효과(Glitch/Scanline Effect)가 적용된다.

### B. Growth Tier Comparison Table Component
*   **기본 구조:** 3열 비교표 (Basic $\rightarrow$ Pro $\rightarrow$ Growth Engine).
*   **핵심 컴포넌트: Feature Card:** 각 기능 설명은 단순히 체크박스가 아닌, **'Icon + 짧은 문구 + 부연 설명(Tooltip)'**으로 구성한다.
*   **Growth Logic 시각화 (최상):** '핵심 결과물' 열의 Growth Engine 항목은 단순 텍스트가 아니다. 반드시 **'성장 곡선 그래프 컴포넌트(Uptrend Curve)'**를 사용해야 하며, 이 그래프는 y축 단위에 따라 마우스 오버 시 실제 수치(예: $50 \rightarrow $250 $\rightarrow$ $500)가 툴팁으로 표시되어야 한다.

### C. Call-to-Action (CTA) Block Component
*   **활용:** 페이지 전반에 걸쳐 최소 3회 이상 사용을 의무화한다.
*   **Primary CTA Button:** 배경색(Solid), Corner Radius 8px, Transition 효과 적용. (`#FF6B3D` / White).
*   **Secondary CTA Link:** 버튼이 아닌 밑줄 형태의 링크로 처리하며, 마우스 오버 시 색상이 Orange Coral로 바뀌고 아래에 점선 언더라인이 생겨나야 한다.

## ⚙️ 4. 개발 시스템 및 확장성 가이드 (System & Scalability)
*   **기술 스택:** Next.js 기반 컴포넌트 아키텍처를 따른다. 모든 UI는 재사용 가능한 React Component로 분리되어야 함.
*   **접근성 (Accessibility):** 모든 폰트와 색상 조합은 WCAG AA 레벨 이상의 대비율을 충족해야 한다. 특히 Deep Navy 배경 위에서 Orange Coral 강조색 사용 시, 명암 대비를 반드시 체크한다.
*   **반응형(Responsiveness):** 데스크톱/태블릿/모바일 세 가지 뷰포트 모두를 기준으로 컴포넌트를 설계하고, 모바일에서는 '비교표'가 카드 형태(Vertical Stack)로 자연스럽게 재배열되도록 합니다.

***
[최종 확인] 본 명세서는 모든 에이전트가 참조하는 **"D.AAL DESIGN 공식 UI/UX 가이드"** 역할을 수행하며, 향후 어떤 콘텐츠를 추가하든 이 시스템을 벗어나지 않아야 함.