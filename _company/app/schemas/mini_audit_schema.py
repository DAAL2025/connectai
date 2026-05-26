from pydantic import BaseModel, Field
from typing import Optional

# --- 1. 입력 데이터 모델 (Input Validation Source) ---
class AuditInput(BaseModel):
    """Mini-Audit Funnel에서 수집하는 핵심 비즈니스 지표들을 정의합니다."""
    website_url: str = Field(..., description="사용자가 제출한 웹사이트의 URL.")
    monthly_revenue_usd: float = Field(..., ge=0, description="최근 월 평균 매출액 (USD). 음수 불가.")
    conversion_rate_percent: float = Field(..., ge=0.1, le=100, description="현재 전환율 (%). 최소 0.1% 이상이어야 함.")
    traffic_change_pct: Optional[float] = Field(None, description="지난 기간 대비 트래픽 변화율 (%)")
    payment_flow_issues: Optional[int] = Field(None, ge=0, description="결제 플로우에서 감지된 문제 지표 수.")

# --- 2. 출력 결과 데이터 모델 (Standardized Output) ---
class FailureCostReport(BaseModel):
    """Failure Cost 계산 엔진의 최종 보고서 구조."""
    failure_cost_score: float = Field(..., description="종합적인 재무적 손실 비용 점수 (0-100). 높을수록 위험함.")
    risk_level: str = Field(..., description="위험 수준 ('Low', 'Medium', 'High', 'Critical').")
    suggested_action: str = Field(..., description="가장 먼저 취해야 할 구체적인 액션 단계 (예: '결제 플로우 최적화').")
    detailed_analysis: dict = Field(..., description="지표별 분석 내용 상세 데이터.")