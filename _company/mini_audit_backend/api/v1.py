from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import User # 가정한 모델 임포트
from ..services.payment_service import MiniAuditService, StripePaymentService, PayPalPaymentService

# Dependency Injection (DB 세션 및 서비스 인스턴스를 받도록 설정)
def get_db():
    # 실제로는 DB 연결 풀에서 세션을 가져옴
    print("⚙️ [Dependency] Database Session Started.")
    return object() # Mockup이므로 객체 반환

router = APIRouter(prefix="/mini-audit/v1", tags=["MiniAudit"])

@router.post("/submit")
def submit_mini_audit(
    # 요청 바디: 손실 비용, 리스크 레벨, 상세 데이터
    loss_cost: float, 
    risk_level: str, 
    audit_details: dict,
    db: Session = Depends(get_db)
):
    """Mini-Audit Funnel의 결과를 받아 DB에 기록하고 감사 이력을 생성하는 엔드포인트."""
    # 실제 환경에서는 JWT 등을 통해 user_id를 가져와야 함. 여기선 Mockup으로 1을 사용.
    MOCK_USER_ID = 1 

    try:
        service = MiniAuditService(db)
        result = service.submit_audit_result(MOCK_USER_ID, loss_cost, risk_level, audit_details)
        return {"status": "Success", "message": f"Mini-Audit 결과가 성공적으로 기록되었습니다. (Risk: {risk_level})", "result_id": result.id}

    except Exception as e:
        print(f"🚨 Error submitting audit: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during audit submission.")


@router.post("/subscribe")
def process_subscription(
    user_id: int, 
    amount: float, 
    payment_gateway_type: str, # 'stripe' or 'paypal'
    payment_token: str, # Stripe/PayPal에서 발행된 토큰
    db: Session = Depends(get_db)
):
    """구독 결제를 처리하고 감사 이력을 기록하는 엔드포인트."""
    if payment_gateway_type == "stripe":
        pg = StripePaymentService("sk_mock")
    elif payment_gateway_type == "paypal":
        pg = PayPalPaymentService("client_id_mock")
    else:
        raise HTTPException(status_code=400, detail="Unsupported payment gateway.")

    try:
        service = MiniAuditService(db)
        result = service.purchase_subscription(user_id, amount, pg, payment_token)
        return {"status": "Success", "message": result['message'], "details": result['details']}
    except Exception as e:
        print(f"🚨 Error processing subscription: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during payment process.")