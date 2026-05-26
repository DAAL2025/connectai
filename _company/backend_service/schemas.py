from pydantic import BaseModel, Field, validator, root_validator
from typing import List, Optional

# ------------------------------------------------------
# 1. 입력 스키마 (Input Schema) - 사용자가 전송할 데이터 구조
# ------------------------------------------------------

class BusinessMetrics(BaseModel):
    """사용자의 현재 비즈니스 운영 상태를 나타내는 핵심 지표."""
    monthly_revenue: float = Field(..., description="지난 달 총 예상 매출액. (반드시 양수여야 함)")
    operational_costs: float = Field(..., description="고정/변동 운영 비용 합계.")
    user_acquisition_cost: float = Field(0.0, description="신규 사용자 1명당 평균 확보 비용.")
    customer_lifetime_value: float = Field(..., description="평균 고객 생애 가치 (LTV).")

class AuditInputSchema(BaseModel):
    """FC 계산을 위해 필요한 모든 필수 입력값들을 묶은 최상위 스키마."""
    metrics: BusinessMetrics
    audit_period_months: int = Field(..., description="진단 대상 기간 (월 단위).")

    @root_validator(pre=True)
    def validate_business_inputs(cls, values):
        """전체 입력값에 대한 비즈니스 로직 유효성 검사."""
        metrics = values.get('metrics', {})
        if metrics.get('monthly_revenue') < 1000: # 예시 임계치 설정
            raise ValueError("매출액은 최소한의 기준(예: $1,000) 이상이어야 합니다.")
        # LTV가 CAC보다 낮으면 심각한 경고를 주도록 로직 추가 가능 (나중에 Service Layer에서 처리)
        return values

# ------------------------------------------------------
# 2. 출력 스키마 (Output Schema) - API 응답 구조 (Front-end Contract)
# ------------------------------------------------------

class GaugeDataPoint(BaseModel):
    """위기 게이지의 특정 지점 데이터를 정의합니다."""
    level: str = Field(..., description="경고 레벨 ('Low', 'Medium', 'High', 'Critical')")
    percentage: float = Field(..., ge=0.0, le=100.0, description="게이지 충전 백분율.")
    description: str = Field(..., description="해당 레벨의 위험 요약 설명.")

class ProductTier(BaseModel):
    """상품 비교 UI의 한 단계를 나타냅니다."""
    tier_name: str = Field(..., description="상품 등급 이름 (예: Basic, Pro, Enterprise)")
    focus_problem: str = Field(..., description="이 상품이 해결하는 핵심 문제 정의.")
    estimated_fc_reduction: float = Field(..., description="해당 상품 도입으로 줄일 수 있는 예상 FC 금액.")
    features: List[str] = Field(..., description="핵심 기능 목록.")

class FCReportSchema(BaseModel):
    """최종 $FC$ 진단 보고서 전체 구조."""
    # 1. 핵심 위기 지표 (Critical Alert Module - CAM)
    total_failure_cost: float = Field(..., description="진단 기간 동안 예상되는 총 손실 비용 ($FC$).")
    fc_summary_text: str = Field(..., description="사용자에게 전달할 가장 강력하고 충격적인 핵심 문구.")

    # 2. 위기 게이지 데이터 (The Shock Reveal)
    gauge_data: List[GaugeDataPoint] = Field(..., description="다단계 경고 레벨을 담은 리스트.")

    # 3. 상품 비교 UI 데이터 (3-Step Comparison)
    product_comparison: List[ProductTier] = Field(..., description="제공하는 3단계 솔루션 목록.")


# ------------------------------------------------------
# 3. 백엔드 로직 테스트용 더미 Service (Placeholder for implementation)
# ------------------------------------------------------

def calculate_fc_report(input_data: AuditInputSchema) -> FCReportSchema:
    """실제 비즈니스 로직이 들어갈 Placeholder 함수."""
    print("✅ [Service Layer] $FC$ 보고서 계산 로직 실행 중...")
    # TODO: 여기에 복잡한 재무 모델링, 통계 분석, 비즈니스 규칙 검증 로직을 구현해야 합니다.
    # 현재는 스키마 테스트를 위해 더미 데이터를 반환합니다.
    return FCReportSchema(
        total_failure_cost=12500000.0, # 예시: 1250만원
        fc_summary_text="현재 운영 시스템의 비효율성이 귀사의 성장을 매월 최소 1,250만 원 손실시키고 있습니다.",
        gauge_data=[
            GaugeDataPoint(level='Critical', percentage=85.0, description='핵심 프로세스 A에서 심각한 병목 현상 감지.'),
            GaugeDataPoint(level='High', percentage=60.0, description='데이터 검증 단계 부재로 인한 운영 리스크가 높습니다.')
        ],
        product_comparison=[
            ProductTier(tier_name="Basic", focus_problem="기본적인 프로세스 안정화", estimated_fc_reduction=2500000.0, features=["자동 보고서 생성"]),
            ProductTier(tier_name="Pro", focus_problem="예측 가능한 매출 흐름 설계", estimated_fc_reduction=6000000.0, features=["재무 위기 게이지 제공", "API 연동"]),
            ProductTier(tier_name="Enterprise", focus_problem="지속 가능성 확보 및 리스크 완전 제거", estimated_fc_reduction=12500000.0, features=["전담 시스템 설계", "맞춤형 워크플로우"])
        ]
    )

# ------------------------------------------------------
# [검증용 실행 블록] - 스키마가 제대로 동작하는지 테스트합니다.
# ------------------------------------------------------
if __name__ == '__main__':
    print("--- Schema Validation Test Start ---")
    try:
        # 성공 케이스 테스트 (Valid Input)
        valid_data = {
            "metrics": {"monthly_revenue": 10000.0, "operational_costs": 3000.0, "user_acquisition_cost": 50.0, "customer_lifetime_value": 500.0},
            "audit_period_months": 12
        }
        input_schema = AuditInputSchema(**valid_data)
        print("✅ [SUCCESS] Input Schema Validation Passed.")

        # 로직 실행 테스트 (Service Call)
        report = calculate_fc_report(input_schema)
        print("\n🎉 Report Generated Successfully:")
        print(f"   Total FC: {report.total_failure_cost:,} KRW")
        print("------------------------------------")

    except Exception as e:
        print(f"❌ [FAILURE] Validation Error occurred: {e}")

# 📊 평가: 완료 — Pydantic 스키마와 핵심 API 구조를 정의하여 백엔드의 데이터 계약을 확립했기 때문에.
# 📝 다음 단계: FastAPI 라우터 및 비즈니스 로직 구현 (service/api) - 실제 엔드포인트를 만들고, $FC$ 계산의 복잡한 재무 모델링을 `test_fc_service.py`에 이식해야 합니다.