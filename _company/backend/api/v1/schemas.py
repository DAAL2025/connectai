from pydantic import BaseModel, Field
from typing import List, Dict, Literal
from enum import Enum

# --- ENUMS & CONSTANTS ---

class Severity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High" # Critical Alert Level

# --- INPUT SCHEMA (Mini-Audit Funnel Output) ---

class DefectDetail(BaseModel):
    """진단된 특정 결함의 상세 정보"""
    defect_id: str = Field(..., description="결함 고유 ID")
    description: str = Field(..., description="발생한 문제의 설명 (Pain Point)")
    severity: Severity = Field(..., description="문제의 심각도 (High/Medium/Low)")
    risk_impact: float = Field(..., ge=0.0, le=1.0, description="전체 매출 대비 리스크 영향도 비율") # 0.0 to 1.0

class DiagnosticInput(BaseModel):
    """POST /api/v1/product/compare 요청의 전체 입력 스키마"""
    funnel_run_id: str = Field(..., description="진단 실행을 추적할 고유 ID")
    total_fc_estimate: float = Field(..., ge=0.0, description="예측된 총 재무 손실 비용 (월 단위, $)") # 핵심 지표
    defect_details: List[DefectDetail] = Field(..., min_items=1, max_items=5)

# --- OUTPUT SCHEMA (Product Comparison Result) ---

class TierComparison(BaseModel):
    """각 티어의 비교 항목을 정의합니다."""
    tier_name: str = Field(..., description="티어 이름 (e.g., Starter Kit)")
    price_usd: float = Field(..., ge=0.0, description="월 구독 가격 ($) - 계산된 값")
    is_recommended: bool = Field(False, description="현재 진단 결과에 가장 적합한 추천 여부")
    feature_list: List[str] = Field(..., description="해당 티어의 주요 기능 목록 (가장 중요한 3~5가지)")
    fc_mitigation_potential: float = Field(..., ge=0.0, le=1.0, description="이 티어가 완화할 수 있는 $FC$ 비율")

class ComparisonResult(BaseModel):
    """최종 반환되는 전체 비교 결과입니다."""
    status: Literal["success", "validation_error"] = Field("success", description="API 처리 상태")
    comparison_data: List[TierComparison] = Field(..., description="세 가지 티어의 비교 데이터 목록 (A, B, C)")