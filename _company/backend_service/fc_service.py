from pydantic import BaseModel, Field, validator
from typing import Literal, Optional
import random

# ------------------------------------------
# 1. 데이터 스키마 정의 (Pydantic Models)
# ------------------------------------------

class FinancialLossCost(BaseModel):
    """
    API 요청 본문에서 받을 $FC$ 계산에 필요한 핵심 입력 데이터 모델.
    모든 필드는 Null을 허용하지 않는다는 가정을 합니다.
    """
    user_id: str = Field(..., description="시스템 식별자 (사용자/클라이언트 ID)")
    client_industry: str = Field(..., min_length=3, max_length=50, description="클라이언트가 속한 산업군")
    current_revenue_monthly: float = Field(..., ge=0.0, description="현재 월별 매출액 (원)")
    operational_cost_monthly: float = Field(..., ge=0.0, description="현재 월별 운영 비용 (원)")
    historical_growth_rate: Optional[float] = Field(None, description="과거 평균 성장률 (%)")

class AlertStatus(BaseModel):
    """
    API 응답 본문에서 돌려줄 최종 경고 상태 정의.
    'Normal', 'Warning', 'Crisis' 세 가지 레벨만 가능합니다.
    """
    status: Literal["Normal", "Warning", "Crisis"]
    message: str = Field(..., description="해당 상태에 대한 사용자 친화적 안내 메시지")

class FCResult(BaseModel):
    """
    API의 최종 성공 응답 구조.
    """
    fc_value: float = Field(..., ge=0.0, description="예상되는 재무적 손실 비용 (원)")
    status: AlertStatus
    metadata: dict = Field({}, description="추가적인 분석 데이터 또는 로그 정보")

# ------------------------------------------
# 2. 비즈니스 로직 구현 (Service Layer)
# ------------------------------------------

def calculate_fc(data: FinancialLossCost) -> FCResult:
    """
    [CORE LOGIC] 재무적 손실 비용($FC$)을 예측하는 핵심 비즈니스 함수입니다.
    이곳에 실제 복잡한 ML/AI 모델 연동 로직이 들어갑니다. (Mocking된 부분)

    Args:
        data: 클라이언트의 현재 재무 데이터(FinancialLossCost).

    Returns:
        FCResult: 계산된 $FC$ 값과 경고 상태를 담은 결과 객체.
    """
    # --- [Validation Check] ---
    if data.current_revenue_monthly < 100000.0 and data.operational_cost_monthly > 200000.0:
        # 예외적인 데이터 조합에 대한 강제 경고 로직 (규칙 기반)
        alert = "매출 대비 고정 비용이 과도하게 높아 재무적 리스크가 매우 높습니다."
        fc_value = data.operational_cost_monthly * 1.5 + random.uniform(50000, 100000) # 패닉 유도 값
        status = "Crisis"
    # --- [Mock Calculation] ---
    else:
        # Mock Logic: (운영 비용 - 매출)의 누적값에 성장률 페널티를 더해 $FC$ 예측.
        base_risk = data.operational_cost_monthly - data.current_revenue_monthly
        fc_value = abs(base_risk) * (1 + (data.historical_growth_rate or 0) / 100)
        
        # --- [Status Determination] ---
        if fc_value >= 12000000: # 1,200만 원 기준
            status = "Crisis"
            message = f"🚨 심각한 재무적 위기 상태입니다. 최소 {fc_value:,.0f}원의 손실이 예측됩니다."
        elif fc_value >= 5000000: # 500만 원 기준
            status = "Warning"
            message = f"⚠️ 경계 단계입니다. 운영 리스크를 점검하지 않으면 {fc_value:,.0f}원 이상의 손실이 예상됩니다."
        else:
            status = "Normal"
            message = "✅ 재무 구조가 안정적이나, 잠재적 위험을 방지하기 위한 미니-감사(Mini-Audit)를 권장합니다."

    # 결과 반환
    return FCResult(
        fc_value=round(fc_value, 2),
        status=AlertStatus(status=status, message=message),
        metadata={"calculation_date": "2026-05-26"} # 로직 실행 시점을 기록하는 것이 좋음.
    )

# ------------------------------------------
# 테스트 코드 (Mock Testing Block)
# ------------------------------------------
if __name__ == "__main__":
    print("="*50)
    print("💰 $FC$ Prediction Service Test Start")
    print("="*50)

    # Case 1: Normal Scenario (모의 데이터 테스트)
    good_data = FinancialLossCost(
        user_id="test-user-A",
        client_industry="SaaS",
        current_revenue_monthly=3000000, # 매출 높음
        operational_cost_monthly=1500000, # 비용 낮음
        historical_growth_rate=5.0
    )
    result_normal = calculate_fc(good_data)
    print("\n[테스트 1: 정상 구조 (Normal)]")
    print(f"  입력 데이터 유효성 검사 성공: {good_data.model_dump()}")
    print(f"  결과값 (FC): {result_normal.fc_value:,.0f}원 | Status: {result_normal.status.status}")

    # Case 2: Crisis Scenario (위기 상황 시뮬레이션)
    crisis_data = FinancialLossCost(
        user_id="test-user-B",
        client_industry="E-commerce",
        current_revenue_monthly=500000, # 매출 극히 낮음
        operational_cost_monthly=2000000, # 비용 높음 (매출 대비 4배)
    )
    result_crisis = calculate_fc(crisis_data)
    print("\n[테스트 2: 위기 구조 (Crisis)]")
    print(f"  입력 데이터 유효성 검사 성공: {crisis_data.model_dump()}")
    print(f"  결과값 (FC): {result_crisis.fc_value:,.0f}원 | Status: {result_crisis.status.status}")

    # Case 3: Input Validation Fail Test (Pydantic 검증 테스트)
    try:
        bad_data = FinancialLossCost(user_id="fail", client_industry="X", current_revenue_monthly=-100, operational_cost_monthly=100) # revenue < 0
        calculate_fc(bad_data)
    except Exception as e:
        print("\n[테스트 3: 유효성 검사 실패 (Expected Error)]")
        # Pydantic이 알아서 에러를 발생시키는지 확인하는 것만으로 충분함.
        pass