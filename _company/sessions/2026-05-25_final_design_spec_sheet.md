# 🎨 D.AAL DESIGN 웹사이트 최종 UI/UX 설계 명세서 (v1.0)

**목표:** 단순한 '웹페이지'가 아닌, 고객의 Pain Point를 자극하고, 우리 시스템의 가치(MRR, 성장 로직)를 직관적으로 인지시켜 계약을 유도하는 **'비즈니스 운영 시스템' 랜딩 페이지 구현**.

## ⚙️ I. 전역 디자인 시스템 (Global Design System)

*   **Primary Color:** `#0A1931` (딥 네이비). 배경, 본문 요소의 주 색상으로 사용. [근거: 자율 사이클 메모리]
*   **Action/Accent Color:** `#FF6B3D` (오렌지 코랄). CTA 버튼, 핵심 데이터 플로우(화살표), 수익 강조 부분에만 제한적으로 사용. [근거: 자율 사이클 메모리]
*   **Typography:** Inter 또는 Pretendard 계열의 산세리프 폰트 사용을 기본으로 하며, Heading은 Bold 처리를 극대화하여 시스템적 느낌을 부여합니다.
*   **전반적인 톤앤매너 (Tone & Manner):** '정교함', '데이터 기반', '운영 시스템'. 배경에 미묘하게 움직이는 그리드(Grid) 패턴 또는 데이터 흐름(Data Flow) 애니메이션을 깔아 정적이지 않은 느낌을 부여해야 합니다. [근거: Self-RAG]

## 🚀 II. 섹션별 UI/UX 통합 명세 (Section Component Breakdown)

### 1. 히어로 영역 (Hero Section) - (Above the Fold)
*   **H1:** "단순한 웹사이트를 넘어, 성과를 측정하는 비즈니스 운영 시스템을 구축합니다." [근거: Designer Self-RAG]
*   **H2:** "D.AAL DESIGN은 코드를 판매하지 않습니다. 지속 가능한 성장 로직(Growth Logic)을 설계하고 구현합니다." [근거: Designer Self-RAG]
*   **UI/UX 핵심 요소 (필수 인터랙션):**
    1.  **배경 애니메이션:** 배경에 움직이는 데이터 흐름(Data Flow) 애니메이션 또는 그래프가 미묘하게 깔려야 합니다. 스크롤 시 이 데이터 플로우의 밀도가 높아지며 '시스템 가동' 느낌을 줘야 합니다. [근거: Self-RAG]
    2.  **CTA 강화:** CTA 버튼(`무료 시스템 감사 요청`) 옆에 작은 아이콘으로 **'MRR 예측(Monthly Recurring Revenue)'** 개념 시각화 그래프를 배치합니다. 마우스를 올리면 간단한 성장 곡선이 팝업되는 인터랙션 추가. [근거: Self-RAG]

### 2. Pain Point/문제 정의 섹션 (The Problem)
*   **목적:** 기존 방식의 한계를 인지시키고, D.AAL DESIGN만이 가진 '시스템' 관점의 필요성을 공감하게 한다.
*   **UI/UX 핵심 요소:**
    1.  **시각적 대비 (Contrast):** 이 섹션은 의도적으로 **회색 톤과 Glitch(깨짐) 효과**를 사용합니다. 이는 기존 방식이 '정체'되고 '손상됨'을 시각화합니다. [근거: Self-RAG]
    2.  **경고 아이콘:** 기술 부채 관련 텍스트 옆에는 지속적인 경고 아이콘(⚠️)을 배치하여 심리적 위협감을 조성합니다. [근거: Self-RAG]
    3.  **전환 지점 (The Pivot):** 이 섹션이 끝나고 D.AAL DESIGN의 솔루션(`D.AAL ENGINE` 도입)으로 진입하는 순간, 배경 톤은 급격히 **딥 네이비(#0A1931)**로 정돈되며 깨짐 효과가 사라져야 합니다.

### 3. 가치 비교 및 성장 로직 (Growth Logic Comparison Table)
*   **제목:** D.AAL DESIGN의 4단계 성장 로직 설계 프로세스 [근거: Self-RAG]
*   **핵심 시각화 (The Money Shot):** 일반적인 웹사이트와 저희 시스템을 비교하는 표에서, '핵심 결과물' 열은 단순히 텍스트가 아닌 **성장 곡선 그래프(Uptrend Curve)** 형태로 시각화해야 합니다. 이 그래프는 시간이 지날수록 가파르게 우상향합니다. [근거: Self-RAG]
*   **수익 강조:** MRR 관련 수치나 성장 추이와 관련된 모든 요소는 오렌지 코랄(#FF6B3D)로 포인트를 주어 '수익'과 직결시킵니다. [근거: Self-RAG]

### 4. Growth Tier / 결제 및 구독 섹션 (Conversion Zone)
*   **상품 구성:** 세 개의 티어 카드(Basic $\rightarrow$ Professional $\rightarrow$ **Growth Engine**)를 배치합니다. 'Growth Engine' 카드는 가장 크고 중앙에 위치하며, 시각적 무게중심이 되어야 합니다. [근거: 자율 사이클 메모리]
*   **최종 인터랙션 (가장 중요):** 사용자가 'Growth Engine Retainer' 카드를 선택하거나 CTA를 클릭하는 순간, 단순히 금액이 제시되는 것이 아니라 **'월간 수익 예상 시뮬레이터(Interactive Simulator)'**와 같은 요소를 띄워야 합니다.
    *   **시뮬레이션 내용:** (예: "현재 웹사이트 트래픽 X명 $\rightarrow$ 저희 시스템 도입 후 Y% 증가 예측 $\rightarrow$ 월 예상 추가 매출 Z원")
    *   **추가 문구:** 결제 버튼 바로 위 또는 근처에 작은 문구로 **"MRR 기반의 지속 가능한 투자"**를 배치하여, 이 구매가 비용이 아닌 '성장 로직 투자'임을 상기시킵니다. [근거: Self-RAG]

### 5. 프로세스 및 신뢰 구축 섹션 (The Process)
*   **섹션 제목:** D.AAL DESIGN의 3단계 성장 로직 설계 프로세스 (Audit $\rightarrow$ Logic $\rightarrow$ Build) [근거: Self-RAG]
*   **Step 1 (Audit):** 'Before State'를 강조하며, 녹색 경고 아이콘(⚠️)과 깨진 파선 느낌으로 진단하는 과정을 시각화합니다. CTA는 "무료 시스템 감사 요청"입니다. [근거: Self-RAG]
*   **Step 2 (Logic - 핵심):** 배경에 복잡하지만 깔끔하게 정리된 **'데이터 플로우 다이어그램'**을 배치합니다. 화살표는 오렌지 코랄(#FF6B3D)로 강조하며, 데이터와 돈의 흐름(Flow of Money & Data)을 시뮬레이션하는 느낌이 가장 강해야 합니다. [근거: Self-RAG]
*   **Step 3 (Build):** 좌측에는 깔끔한 웹사이트 시안을, 우측에는 그 기반이 되는 '아키텍처 다이어그램(Next.js Stack)'을 나란히 배치하여 기술력과 결과물을 동시에 보여줍니다. [근거: Self-RAG]

---
**[Attached Asset]:** 최종 디자인 스펙에 따라 제작된 Figma 파일은 다음 경로를 참조하십시오.
/Volumes/daal/Documents/01.Work/connect ai/_company/sessions/2026-05-25_final_design_spec_sheet.fig