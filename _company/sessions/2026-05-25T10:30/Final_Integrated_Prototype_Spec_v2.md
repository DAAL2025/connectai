# 🎨 D.AAL DESIGN 통합 프로토타입 명세서 (V2.0)

## 🎯 목표
LAI 인터랙티브 시뮬레이터와 오류 처리 컴포넌트를 포함한 최종 랜딩 페이지의 End-to-End 사용자 경험(UX)을 확정하고, 개발팀이 즉시 구현할 수 있는 통합 Figma 스펙을 제공합니다. (최종 QA 로드맵 반영)

## 🌐 구조 개요
*   **레이아웃:** Full Width, Sticky Navigation 적용.
*   **컬러 팔레트:** 주조색: Deep Navy (#0A1931). 강조색: Orange Coral (#FF6B3D). 경고/에러: Reddish Gray (⚠️).

## 🧱 섹션별 명세 및 컴포넌트 매핑

### 1. Hero Section (Initial View)
*   **H1:** "단순 웹사이트를 넘어, 성과를 측정하고 예측하는 비즈니스 운영 시스템을 구축합니다."
    *   [근거: Self-RAG]
*   **시각 요소:** 배경에 미묘한 Data Flow 애니메이션(Dark/Subtle) 적용.
*   **CTA 1 (Primary):** "무료 시스템 감사 요청" (LAI Simulator로 스크롤 이동 트리거).

### 2. LAI Interactive Simulator (핵심 전환 지점)
*   **역할:** 사용자의 Pain Point를 자극하고, D.AAL DESIGN의 가치를 체감하게 하는 인터랙티브 컴포넌트입니다.
*   **상호작용:**
    1.  사용자가 '진단 데이터' (가상의 현황 입력)를 넣습니다.
    2.  시뮬레이터가 즉각적으로 **'Loss Avoidance Index (LAI)'** 값을 계산하여 그래프로 보여줍니다. (Orange Coral 강조).
    3.  [성공 경로] LAI가 높을수록, "예상 손실 비용"이 낮아지는 시나리오를 애니메이션으로 제시합니다.
*   **⚠️ 에러 상태 연동:** 이 컴포넌트의 데이터 호출 과정에서 API 오류(4xx/5xx)가 발생하면, **[Error Handler Component]**가 즉시 오버레이됩니다. (최우선 테스트 지점).

### 3. Growth Tier 비교표 (Conversion Point)
*   **구조:** 3단 테이블 (Basic $\rightarrow$ Standard $\rightarrow$ Premium).
*   **핵심 시각화:** '결과물' 열은 정적인 텍스트가 아닌, **시간에 따른 MRR 성장 곡선(Uptrend Curve)** 그래프로 구현됩니다. (Premium Tier만 최고점 기록).
    *   [근거: Self-RAG]
*   **CTA 2 (Secondary):** "맞춤 견적 요청" → 이 버튼 클릭 시, 결제/견적 시스템으로 이동합니다.

### 4. Error Handling Component (Critical UX Path)
*   **트리거:** LAI Simulator의 데이터 호출 실패 또는 결제 모듈 연동 실패 등 모든 백엔드 오류 발생 시 활성화됩니다.
*   **디자인 스펙:** 단순 '오류 메시지'가 아닌, **"현재 진단 과정에서 시스템적 이슈가 감지되었습니다. [이유]를 확인하고 다음 행동을 취해주세요."** 형태의 학습형 실패 경험 제공. (Self-RAG/Developer Memory 반영)
*   **필수 요소:** 오류 코드(예: 412 - 비즈니스 로직 불일치), 해결 가이드라인, 재시도 버튼 배치.

## 🚀 개발팀 참고 사항 (Codari 대상)
1.  **데이터 플로우 우선순위:** LAI 계산 로직과 에러 핸들링 로직의 연동이 최우선 검증되어야 합니다. 성공/실패 시 UI 변화가 매끄럽고 의미론적으로 일치해야 합니다.
2.  **상태 관리:** 모든 컴포넌트(LAI, Growth Tier)는 동일한 전역 상태 관리 시스템을 공유하여 데이터의 일관성을 유지합니다.