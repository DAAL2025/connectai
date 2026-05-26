import pytest
from mini_audit_backend.services.payment_service import StripePaymentService, PayPalPaymentService

# ------------------------------------------
# Mocking DB Session for Unit Test Isolation
# (실제 테스트 시에는 SQLAlchemy InMemory 엔진 사용 권장)
class MockDBSession:
    pass

def test_stripe_success():
    """Stripe의 성공적인 결제 플로우를 테스트한다."""
    service = StripePaymentService("sk_test_mock")
    result = service.process_payment(user_id=1, amount=99.99, token="tok_visa")
    assert result['success'] is True
    assert "stripe_" in result['transaction_id']

def test_stripe_failure():
    """Stripe의 실패적인 결제 플로우를 테스트한다."""
    service = StripePaymentService("sk_test_mock")
    # 잘못된 토큰이나 0 금액으로 강제 실패 유도
    result = service.process_payment(user_id=1, amount=0.00, token="invalid_token")
    assert result['success'] is False
    assert "Invalid payment details" in result['error']

def test_paypal_success():
    """PayPal의 성공적인 결제 플로우를 테스트한다."""
    service = PayPalPaymentService("client_id_test")
    result = service.process_payment(user_id=2, amount=19.99, token="pp_visa")
    assert result['success'] is True
    assert "paypal_" in result['transaction_id']

def test_paypal_failure():
    """PayPal의 실패적인 결제 플로우를 테스트한다."""
    service = PayPalPaymentService("client_id_test")
    result = service.process_payment(user_id=2, amount=0.00, token="invalid_token")
    assert result['success'] is False