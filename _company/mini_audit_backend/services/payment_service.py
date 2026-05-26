from abc import ABC, abstractmethod
from typing import Dict, Any

# --- Abstract Base Class: 모든 결제 게이트웨이의 계약(Contract) ---
class PaymentGateway(ABC):
    """모든 PG는 이 인터페이스를 구현해야 한다."""
    @abstractmethod
    def process_payment(self, user_id: int, amount: float, token: str) -> Dict[str, Any]:
        """실제 결제를 처리하고 결과를 반환한다. (Mockup 필수)"""
        pass

# --- 1. Stripe 구현체 ---
class StripePaymentService(PaymentGateway):
    def __init__(self, api_key: str):
        self.api_key = api_key # 실제 키 사용 금지! 환경변수에서 로드해야 함

    def process_payment(self, user_id: int, amount: float, token: str) -> Dict[str, Any]:
        print(f"⚡️ [Stripe] User {user_id}에게 ${amount:.2f} 결제 시도 (Token: {token[:4]}...)")
        # 실제 API 호출 로직이 들어갈 자리
        if amount > 0 and token.startswith("tok_"):
            return {"success": True, "transaction_id": f"stripe_{user_id}_{amount}", "message": "Payment successful via Stripe."}
        else:
            return {"success": False, "error": "Invalid payment details or amount.", "transaction_id": None}

# --- 2. PayPal 구현체 ---
class PayPalPaymentService(PaymentGateway):
    def __init__(self, client_id: str):
        self.client_id = client_id # 실제 ID 사용 금지! 환경변수에서 로드해야 함

    def process_payment(self, user_id: int, amount: float, token: str) -> Dict[str, Any]:
        print(f"⚡️ [PayPal] User {user_id}에게 ${amount:.2f} 결제 시도 (Token: {token[:4]}...)")
        # 실제 API 호출 로직이 들어갈 자리
        if amount > 0 and token.startswith("pp_"):
            return {"success": True, "transaction_id": f"paypal_{user_id}_{amount}", "message": "Payment successful via PayPal."}
        else:
            return {"success": False, "error": "Invalid payment details or amount.", "transaction_id": None}

# --- Core Service (비즈니스 로직 통합) ---
class MiniAuditService:
    """Mini-Audit Funnel의 핵심 비즈니스 로직을 처리하는 서비스 레이어."""
    def __init__(self, db_session):
        self.db = db_session

    def submit_audit_result(self, user_id: int, loss_cost: float, risk: str, audit_data: dict) -> MiniAuditResult:
        # 1. 결과 저장 (MiniAuditResult 테이블에 기록)
        new_result = MiniAuditResult(
            user_id=user_id,
            estimated_loss_cost=loss_cost,
            risk_level=risk,
            audit_details=audit_data
        )
        self.db.add(new_result)
        # 2. 데이터 무결성 확보: 감사 이력 기록 (가장 중요!)
        self._log_audit(user_id, "MiniAuditResult", new_result.id, {"cost": loss_cost, "risk": risk}, audit_data)
        self.db.flush() # DB ID를 가져오기 위해 flush
        return new_result

    def purchase_subscription(self, user_id: int, amount: float, payment_gateway: PaymentGateway, token: str) -> Dict[str, Any]:
        # 1. 결제 실행 (외부 서비스 호출)
        payment_response = payment_gateway.process_payment(user_id, amount, token)
        
        if not payment_response['success']:
            return {"status": "Failed", "message": f"Payment failed: {payment_response.get('error')}"}

        # 2. 결제 성공 시 DB 업데이트 및 로그 기록 (원자성 보장 필요)
        print(f"✅ [Service] Payment successful. Updating user subscription status.")
        # TODO: 실제로는 Subscription 테이블과 User 상태를 업데이트하는 로직 추가
        self._log_audit(user_id, "Subscription", 0, {"status": "Paid", "transaction": payment_response['transaction_id']}, {"amount": amount})

        return {"status": "Success", "message": "Subscription activated.", "details": payment_response}

    def _log_audit(self, user_id: int, entity_type: str, entity_id: int, new_data: dict, old_data: dict) -> None:
        """AuditLog를 생성하는 내부 헬퍼 함수."""
        from .models import AuditLog # 순환 참조 방지
        audit = AuditLog(
            entity_type=entity_type,
            entity_id=entity_id,
            changed_by_user_id=user_id,
            old_data=old_data,
            new_data=new_data
        )
        self.db.add(audit)