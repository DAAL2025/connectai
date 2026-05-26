# D.AAL DESIGN Design System Kit v1.0
**목표:** 웹사이트의 모든 컴포넌트를 모듈화하여, 개발팀이 즉시 구현할 수 있는 '재사용 가능 설계 원칙'을 제공합니다.

## 🎨 Global Variables & Tokens (디자인 토큰)
*   **Primary Color:** `#0A1931` (딥 네이비) - 배경, 주요 구조색
*   **Accent/Action Color:** `#FF6B3D` (오렌지 코랄) - CTA 버튼, 핵심 데이터 강조 (MRR 수치, 성장 화살표)
*   **Warning/Pain Color:** `#900C3F` (다크 마젠타) - Pain Point 섹션, 경고 아이콘
*   **Success/Growth Color:** `#2ECC71` (에메랄드 그린) - 성공적인 로직 구현, Step 3 완료 시점
*   **Typography:**
    *   H1: 'Pretendard' Bold (48px)
    *   H2: 'Pretendard' SemiBold (36px)
    *   Body: 'Pretendard' Regular (16px)

## 🏗️ Core Components 정의 (재사용 모듈)

### 1. [Component] Hero Section Module (`/components/HeroSection`)
*   **목적:** 방문자의 시선 사로잡기 및 핵심 가치 전달 (첫인상, H1/H2).
*   **구조:** `[Data Flow Animation Background]` $\rightarrow$ `[H1 Text Block]` $\rightarrow$ `[CTA Group]`
*   **속성:**
    *   `Animation`: 배경에 미묘하게 움직이는 데이터 흐름(Data Flow) 애니메이션 필수. (Static $\rightarrow$ Dynamic 강조).
    *   `CTA Integration`: CTA 버튼 그룹 옆에 **'MRR 예측 시뮬레이터 아이콘'**을 반드시 배치하여, 서비스가 단순 웹사이트가 아닌 '시스템'임을 인지시킴.

### 2. [Component] Growth Tier Comparison Table (`/components/GrowthTable`)
*   **목적:** 기존 방식의 문제점과 D.AAL DESIGN 솔루션의 차별점을 명확히 제시 (전환 유도).
*   **구조:** `[Header]` $\rightarrow$ `[Feature Row] * N`
*   **속성:**
    *   **Critical Feature:** 비교표의 '핵심 결과물' 열은 **텍스트가 아닌, 우상향하는 성장 곡선 그래프(Uptrend Curve)** 형태로 반드시 시각화해야 함. (Growth Logic 증명)
    *   **Emphasis:** MRR 관련 수치 및 성과 지표는 `Accent/Action Color`를 사용하여 강조하며, 툴팁을 통해 "예측 가능한 반복 매출"이라는 설명을 제공함.

### 3. [Component] Growth Engine Card Module (`/components/GrowthCard`)
*   **목적:** 가장 중요한 수익 모델(Retainer)에 대한 집중 및 구매 결정 촉발 (Conversion Point).
*   **구조:** `[Card Container]` $\rightarrow$ `[Tier Name H2]` $\rightarrow$ `[Feature List]` $\rightarrow$ `[Pricing/CTA Block]`
*   **속성:**
    *   `Visual Hierarchy`: 세 가지 Tier 중 **'Growth Engine Retainer' 카드를 가장 크게, 중앙에 배치하고, 배경색을 살짝 다르게 처리하여 집중도를 높여야 함.**
    *   `Interactivity (Critical)`: 가격 제시 영역은 단순히 텍스트가 아니어야 합니다. **마우스 오버 또는 클릭 시 '월간 수익 예상 시뮬레이터' 형태의 인터랙티브 요소를 활성화**시켜, 고객이 자신의 비즈니스에 대입해보는 느낌을 주도록 설계해야 합니다.
    *   `CTA Text`: CTA 버튼 텍스트는 "구매하기"가 아닌, **"MRR 기반 시스템 구축 요청하기"**와 같이 컨설팅적이고 전문적인 용어를 사용합니다.

### 4. [Component] Process Step Module (`/components/ProcessStep`)
*   **목적:** D.AAL DESIGN의 체계적인 프로세스(Audit $\rightarrow$ Logic $\rightarrow$ Build)를 단계적으로 설명.
*   **구조:** `[Step Number]` $\rightarrow$ `[Phase Title H3]` $\rightarrow$ `[Description Text]` $\rightarrow$ `[Visual Aid/Icon]`
*   **속성:** 각 Step의 배경과 아이콘을 통해 '시스템적 사고'를 유도해야 합니다. 특히, **Step 2 (Logic)**는 데이터 플로우 다이어그램(화살표와 노드)을 중심으로 구성하여, 논리적인 흐름이 시각적으로 압도적이게 만들어야 합니다.

## ✨ Action Plan 및 다음 스텝
1.  **디자인 가이드 문서 확정:** 본 `design_system_kit.md`를 최종 디자인 가이드라인으로 확정합니다. (진행중)
2.  **와이어프레임/UX 검증:** 코다리에게 이 컴포넌트들을 기반으로 실제 Next.js의 초기 와이어프레임을 요청하고, 기술적 구현 가능성을 교차 검증해야 합니다.