import unittest
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import app # main에서 정의된 앱을 가져옵니다 (실제 프로젝트 구조에 맞게 조정 필요)

# 임시 스키마 정의 (테스트를 위해 필요한 최소한의 모델만 재정의)
class FinancialInput(BaseModel):
    current_revenue_monthly: float
    opportunity_loss_rate: float
    required_audit_fee: float

# 테스트 클라이언트 설정 (FastAPI 앱을 직접 사용)
client = app.app

# 🚨 주의: 실제로는 'main' 모듈과 'api/v1' 모듈의 구조적 의존성 문제가 발생할 수 있습니다. 
# 여기서는 로직 검증에 초점을 맞춥니다.
class TestFailureCostAPI(unittest.TestCase):

    def test_failure_cost_calculation_success(self):
        """기본적인 실패 비용 계산이 올바르게 작동하는지 테스트합니다."""
        from api.v1.failure_cost_service import calculate_failure_cost # 실제 경로로 수정 필요
        # 매출 10,000만원, 손실률 20% -> 예상 Cost: 100,000 * 0.2 * 1.5 = 3,000,000원
        expected_cost = 3000000.0
        actual_cost = calculate_failure_cost(100000000, 0.2)
        self.assertAlmostEqual(actual_cost, expected_cost, places=2)

    def test_failure_cost_calculation_invalid_input(self):
        """매출액이나 손실률이 음수일 때 예외 처리가 되는지 테스트합니다."""
        from api.v1.failure_cost_service import calculate_failure_cost
        with self.assertRaises(ValueError):
            calculate_failure_cost(-100, 0.2)

    def test_payment_intent_flow_mocking(self):
        """결제 Intent 생성 PoC가 Mock 데이터를 반환하는지 테스트합니다."""
        from api.v1.failure_cost_service import process_payment_intent
        # 실제 키를 사용하지 않았을 때의 모킹 로직 검증
        result = process_payment_intent(100) 
        self.assertIsInstance(result, str)
        self.assertTrue("mock_id" in result)

    def test_api_endpoint_success(self):
        """최종 API 엔드포인트가 성공적으로 요청을 처리하는지 테스트합니다."""
        # 가상의 유효 데이터셋
        payload = {"current_revenue_monthly": 100000000, "opportunity_loss_rate": 0.2, "required_audit_fee": 50}
        headers = {'Content-Type': 'application/json'}

        # POST 요청 시뮬레이션 (Mock 환경에서는 에러 처리가 중요함)
        response = client.post("/api/v1/calculate-and-pay", json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        # payment_intent_id가 Mock ID로 들어오는지 확인
        self.assertIn('mock_id', data['payment_intent_id'])


if __name__ == '__main__':
    unittest.main()