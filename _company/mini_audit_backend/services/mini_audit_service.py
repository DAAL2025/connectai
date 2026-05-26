import uuid
from datetime import datetime
from typing import Dict, Any
from ..models import MiniAuditResult, AuditLog

def calculate_loss_cost(input_data: Dict[str, Any], user_id: int) -> tuple[MiniAuditResult, AuditLog]:
    """
    사용자 입력 데이터를 바탕으로 예상 손실 비용을 계산하고, 해당 과정을 감사 로그로 기록합니다.

    Args:
        input_data: 사용자가 제공한 비즈니스 지표 (예: 월 매출액, 기술 부채 비율 등).
        user_id: Mini-Audit를 수행하는 사용자 ID.

    Returns:
        (MiniAuditResult 객체, AuditLog 객체): 업데이트된 결과와 감사 로그 기록.
    """
    # 1. Loss Cost 계산 로직 (Placeholder - 실제 복잡한 ML 모델 연동 필요)
    try:
        monthly_revenue = float(input_data.get("monthly_revenue", 0))
        tech_debt_ratio = float(input_data.get("technical_debt_ratio", 0))

        # 임시 로직: 손실 비용은 (매출액 * 기술부채 비율) + 기본 리스크 프리미엄에 비례한다고 가정
        base_cost = monthly_revenue * tech_debt_ratio * 1.5
        calculated_loss_cost = round(base_cost, 2)

        # 2. 위험 레벨 결정 로직 (Failure Cost 기준)
        if calculated_loss_cost > monthly_revenue * 0.3: # 예시 임계값: 매출의 30% 초과 손실 시 High Risk
            risk_level = "High"
        elif calculated_loss_cost > monthly_revenue * 0.1:
            risk_level = "Medium"
        else:
            risk_level = "Low"

    except Exception as e:
        # 데이터 타입 오류 등 예외 처리
        calculated_loss_cost = 0.0
        risk_level = "Error"
        print(f"Loss Cost Calculation Error: {e}")


    # 3. MiniAuditResult 객체 생성 및 업데이트 (데이터 무결성 확보)
    updated_result = MiniAuditResult(
        user_id=user_id,
        input_data=input_data,
        calculated_loss_cost=calculated_loss_cost,
        risk_level=risk_level,
        transaction_id=uuid.uuid4() # 새 트랜잭션 ID 부여
    )

    # 4. 감사 로그 생성 (Audit Log 기록 메커니즘의 핵심)
    audit_log = AuditLog(
        user_id=user_id,
        entity_type="MiniAuditResult",
        entity_id=updated_result.transaction_id,
        action="COST_CALCULATION", # 이 액션은 비용 계산 단계임을 명시
        details={"input": input_data, "output": {"cost": calculated_loss_cost, "risk": risk_level}},
        performed_by="System Script: MiniAudit Service"
    )

    return updated_result, audit_log

# TODO: 이 서비스 함수를 API 엔드포인트에서 호출하도록 api/v1.py에 연결해야 합니다.