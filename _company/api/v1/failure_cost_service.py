from pydantic import BaseModel, Field, ValidationError
import random
from typing import Optional, Dict, Any

# --- 1. 데이터 모델 정의 (Input Validation Schema) ---
class FailureCostInput(BaseModel):
    """Mini-Audit 진단에 필요한 핵심 재무 지표를 담는 입력 스키마."""
    failure_cost_type: str = Field(..., description="Failure Cost 유형 ('L' 또는 'O').") # L: Loss, O: Opportunity
    current_metric_value: float = Field(..., gt=0, description="진단 대상 지표의 현재 수치 (e.g., MRR).")
    baseline_period_days: int = Field(..., ge=1, description="비교 기준이 되는 기간 (일 단위).")

# --- 2. 핵심 비즈니스 로직 모듈 (The Core Engine) ---
def calculate_expected_loss(data: FailureCostInput) -> Dict[str, float]:
    """
    실패 비용을 계산하고 예상 손실액(Estimated Loss Amount)을 도출하는 가상 엔진입니다.
    [근거: CEO 지시] - 실패 비용 데이터 기반 Mock API 연동 시뮬레이션
    """
    # 복잡한 재무 로직이 들어가는 부분 (외부 DB/API 호출 시뮬레이션)
    if data.failure_cost_type not in ["L", "O"]:
        raise ValueError("유효하지 않은 Failure Cost 유형입니다.")

    # Loss Cost 계산 로직 예시: 손실액은 현재 수치에 기간과 가중치를 곱함
    loss_factor = 0.15 if data.failure_cost_type == 'L' else 0.25
    estimated_loss = round(data.current_metric_value * loss_factor * (data.baseline_period_days / 30), 2)

    # Opportunity Cost 계산 로직 예시: 기회비용은 현재 수치 대비 잠재적 성장률을 반영함
    if data.failure_cost_type == 'O':
        estimated_loss = round(data.current_metric_value * loss_factor * 1.5, 2)

    return {"estimated_loss": estimated_loss}


# --- 3. API 엔드포인트 로직 (Service Wrapper with Validation Loop) ---
def process_mini_audit_diagnosis(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    사용자 입력을 받아 유효성 검사 루프를 거쳐 실패 비용을 계산하고 
    시스템 감사 필요 여부를 판단하여 결과를 반환합니다.
    """
    print("--- [Service] Starting Failure Cost Diagnosis Process ---")

    # 1. 데이터 유효성 검증 (Validation Loop)
    try:
        validated_data = FailureCostInput(**input_data)
        print(f"✅ [Service] Validation Success. Input data validated.")
    except ValidationError as e:
        # 입력값이 스키마를 위반했을 때의 에러 처리
        return {
            "success": False, 
            "error": "Input Data Validation Failed.",
            "details": str(e),
            "calculated_loss_amount": 0.0,
            "is_audit_required": False
        }

    # 2. 핵심 비즈니스 로직 실행 (Calculation)
    try:
        calculation_result = calculate_expected_loss(validated_data)
        estimated_loss = calculation_result["estimated_loss"]
    except Exception as e:
        return {
            "success": False, 
            "error": f"Internal Calculation Error: {e}",
            "details": str(e),
            "calculated_loss_amount": 0.0,
            "is_audit_required": False
        }

    # 3. 최종 비즈니스 판단 (CTA Decision Logic)
    # 임계값 설정: 손실액이 일정 금액(예: $500) 이상일 경우 System Audit 필요로 판단.
    MINIMUM_AUDIT_THRESHOLD = 500.0
    is_audit_required = estimated_loss >= MINIMUM_AUDIT_THRESHOLD

    # 4. 결과 포맷팅 및 반환
    response = {
        "success": True,
        "message": "Failure Cost Diagnosis Completed.",
        "input_data": validated_data.dict(),
        "calculated_loss_amount": estimated_loss,
        "is_audit_required": is_audit_required,
        "suggested_cta_text": "System Audit 문의하기" if is_audit_required else None
    }
    return response

# 테스트용 실행 코드 (실제 API에서는 라우터가 처리)
if __name__ == '__main__':
    print("\n--- Running Local Test Case 1: High Loss Cost (L, Needs Audit) ---")
    test_case_1 = {"failure_cost_type": "L", "current_metric_value": 3000.0, "baseline_period_days": 30}
    result_1 = process_mini_audit_diagnosis(test_case_1)
    print("\n[Result 1]:")
    import json; print(json.dumps(result_1, indent=2))

    print("\n\n--- Running Local Test Case 2: Low Opportunity Cost (O, No Audit Needed) ---")
    test_case_2 = {"failure_cost_type": "O", "current_metric_value": 50.0, "baseline_period_days": 30}
    result_2 = process_mini_audit_diagnosis(test_case_2)
    print("\n[Result 2]:")
    import json; print(json.dumps(result_2, indent=2))

    print("\n\n--- Running Local Test Case 3: Validation Failure (Missing Field) ---")
    test_case_3 = {"failure_cost_type": "L", "current_metric_value": "INVALID"} # Invalid type
    result_3 = process_mini_audit_diagnosis(test_case_3)
    print("\n[Result 3]:")
    import json; print(json.dumps(result_3, indent=2))