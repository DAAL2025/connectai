# 🚀 Growth Engine Dashboard: 최종 개발 핸드오프 명세서 (Tier $5M)

**[목표]**: 단순 시각적 Mock-up이 아닌, 데이터 기반의 '성장 로직'을 구현하는 시스템의 컴포넌트 레벨 상세 스펙 정의.
**[기준]:** 현빈/코다리의 피드백(Growth Acceleration Ratio, Action Step) 반영 완료.

## 1. 대시보드 전체 구조 및 레이아웃 (Layout System)
*   **Viewport:** Desktop First (1440px 기준). 반응형 가이드라인 포함.
*   **톤앤매너:** 신뢰성(딥 네이비, #0A1931)과 활력(오렌지 코랄, #FF6B3D)의 조합 유지.
*   **핵심 컴포넌트:** 모든 요소는 [Design System Kit]의 컴포넌트를 사용해야 합니다.

## 2. 핵심 섹션별 스펙 상세 (Component Specs)

### A. 히어로 및 KPI 요약 (Hero/KPI Summary - 상단 배너)
*   **요소:** 실시간 'MRR 예측치' 표시 위젯 (가장 중요).
    *   **스펙:** 데이터는 API `GET /api/v1/prediction`에서 받아와야 하며, 7일 단위 추이 그래프(Line Chart Component)로 구현.
    *   **상태 정의:** Loading State, Error State, Empty State를 명시하고, 로딩 시 미묘한 '데이터 흐름' 애니메이션 적용 (Self-RAG 근거).

### B. Growth Acceleration Ratio (GAR) 시각화 영역
*   **요소:** 핵심 성장 지표 분석 위젯 (가장 큰 변화 반영 부분).
    *   **기능/로직:** 단순 수치 표시가 아닌, **'현재 예측 대비 지난 분기의 성장 가속도(%)'를 계산하여 게이지 차트 형태로 시각화.**
    *   **기술 스펙:** 이 지표는 3가지 데이터 포인트 (A: 트래픽 증가율, B: 전환당 평균 수익 개선율, C: 예상 고객 생애가치 상승률)의 가중치 합산으로 계산되어야 함.
    *   **UI/UX 강조:** 게이지 차트의 색상이 오렌지 코랄로 '주의' 또는 '최적 성장 구간'임을 시각적으로 알림.

### C. Action Step & 워크플로우 가이드 (Phase 2, 3 Integration)
*   **요소:** 고객이 즉시 취해야 할 행동 목록 (Action Item List).
    *   **구조:** 비즈니스 에이전트의 Workflow Step 정의를 반영하여, 카드 형태로 구성. 각 카드는 'Step Title', 'Benefit Description', 'Completion Status' 3가지로 나뉨.
    *   **인터랙션:** 사용자가 버튼 클릭 시 (가정), 백엔드 API `POST /api/v1/action_step/{id}/complete` 호출을 트리거하고, 상태(Status)를 변경하는 애니메이션을 구현해야 함.

## 3. 코다리 검증 요청 사항 (Developer Validation Checklist)
*   **API Endpoints:** 위에서 정의된 모든 데이터 포인트가 `GET /api/v1/...` 또는 `POST /api/v1/...` 형태로 호출 가능하도록 백엔드 구조를 재검토해야 합니다.
*   **데이터 모델 업데이트:** 'Growth Acceleration Ratio' 계산을 위한 새로운 가중치 필드(Weighted Factor) 및 관련 추적 데이터 테이블 추가가 필요합니다.