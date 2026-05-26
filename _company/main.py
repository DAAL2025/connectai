from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from .api.v1.failure_cost_service import calculate_failure_cost, process_payment_intent

# .env 파일 로드 (실제 개발 환경에서는 별도의 설정 관리 필요)
load_dotenv() 

app = FastAPI(title="D.AAL Design - Failure Cost API", version="1.0.0")

# --- Pydantic 스키마 정의 ---
class FinancialInput(BaseModel):
    """사용자 입력 기반의 재무 데이터 (예: 예상 트래픽, 전환율 등)"""
    current_revenue_monthly: float # 현재 월 매출액 (원화 기준)
    opportunity_loss_rate: float # 기회 손실률 (%)
    required_audit_fee: float # Mini-Audit 최소 비용

class PaymentResponse(BaseModel):
    """결제 처리 결과 응답 스키마"""
    success: bool
    message: str
    payment_intent_id: str | None = None
    failure_reason: str | None = None

# --- API 엔드포인트 정의 ---

@app.post("/api/v1/calculate-and-pay", response_model=PaymentResponse)
async def calculate_and_process_payment(data: FinancialInput):
    """
    1. Failure Cost 계산 수행 
    2. Stripe Payment Intent 생성 시도 (실제 결제 게이트웨이 연동 PoC)
    3. 결과를 클라이언트에 반환
    """
    try:
        # STEP 1: 실패 비용 계산 (비즈니스 로직 분리)
        failure_cost = calculate_failure_cost(data.current_revenue_monthly, data.opportunity_loss_rate)
        print(f"Calculated Failure Cost: {failure_cost:.2f}원")

        # STEP 2: 결제 게이트웨이 연동 시도 (Stripe Payment Intent 생성 PoC)
        # 실제로는 Webhook을 통해 비동기적으로 결과를 처리해야 하지만, PoC를 위해 즉각적인 Intent 생성을 시도합니다.
        payment_intent = process_payment_intent(data.required_audit_fee)

        if payment_intent:
            return PaymentResponse(
                success=True, 
                message=f"✅ Failure Cost 진단 완료 및 결제 준비 성공! (진단 비용: {data.required_audit_fee:.0f}원)",
                payment_intent_id=payment_intent
            )
        else:
             # 결제 실패 시나리오 처리
            return PaymentResponse(
                success=False, 
                message="❌ 결제 게이트웨이 연동에 실패했습니다. 네트워크 상태를 확인하거나 관리자에게 문의하세요.",
                failure_reason="Payment Intent creation failed."
            )

    except ValueError as e:
        # 입력값 유효성 검증 실패 시 처리 (예: 음수 값 등)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Input Validation Error: {e}")
    except Exception as e:
        # 시스템/API 호출 실패 시 포괄적 에러 핸들링
        print(f"Critical API Failure: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="System Audit 서비스 처리 중 치명적인 오류가 발생했습니다.")

# 참고: 실제 배포 시에는 Webhook 엔드포인트 /api/v1/stripe-webhook 을 별도로 구축해야 합니다.