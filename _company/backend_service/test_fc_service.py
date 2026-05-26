import unittest
from fc_service import calculate_financial_loss_cost, FinancialLossInput

class TestFinancialLossCost(unittest.TestCase):
    """
    FC 계산 로직의 단위 테스트 및 방어적 코딩 검증
    """
    
    def test_successful_calculation(self):
        # 1. 성공 케이스: 유효한 데이터로 정상 계산되는지 확인
        valid_data = {
            "monthly_recurring_revenue": 5000,  # 500만원
            "operational_inefficiency_index": 1.2, # 보통 리스크
            "market_delay_rate": 0.3             # 낮은 지연율
        }
        try:
            validated_input = FinancialLossInput(**valid_data)
            result = calculate_financial_loss_cost(validated_input)
            self.assertEqual(result['status'], 'SUCCESS')
            self.assertIsInstance(result['raw_fc_usd'], float)
        except Exception as e:
            self.fail(f"유효한 데이터로 계산 중 예외 발생: {e}")

    def test_invalid_input_nonexistent_key(self):
        # 2. 실패 케이스 A: 필수 키 누락 (Pydantic validation fail)
        invalid_data = {
            "monthly_recurring_revenue": 5000,
            # 'operational_inefficiency_index' 필드가 누락됨
            "market_delay_rate": 0.3
        }
        _, error = calculate_financial_loss_cost_safe(invalid_data)
        self.assertIsNotNone(error)
        self.assertTrue("구조적 결함 발생 (Structural Flaw Detected)" in error)

    def test_invalid_input_out_of_bounds(self):
        # 3. 실패 케이스 B: 값 범위 초과 (Pydantic validation fail)
        # OEI는 최대 3.0을 넘으면 안됨 (스키마 제한)
        invalid_data = {
            "monthly_recurring_revenue": 5000,
            "operational_inefficiency_index": 4.0, # 범위 초과
            "market_delay_rate": 0.3
        }
        _, error = calculate_financial_loss_cost_safe(invalid_data)
        self.assertIsNotNone(error)
        self.assertTrue("구조적 결함 발생 (Structural Flaw Detected)" in error)

if __name__ == "__main__":
    unittest.main()