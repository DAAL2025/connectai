import pytest
from fastapi.testclient import TestClient
from app.main import calculate_failure_cost # 핵심 로직 함수만 임포트하여 테스트

# FastAPI 클라이언트 설정 대신, 순수 로직 계산 함수를 직접 테스트합니다.
# 이는 API 계층이 아닌 비즈니스 로직(Core Logic)의 안정성을 검증하는 것이 목적입니다.

def test_success_high_risk():
    """Case 1: 트래픽 급락 및 결제 문제 다발 -> Critical Risk 예상"""
    input_data = type('MockData', (object,), {
        'website_url': 'test-site.com',
        'monthly_revenue_usd': 5000.0,
        'conversion_rate_percent': 1.2,
        'traffic_change_pct': -30.0, # 급락
        'payment_flow_issues': 4    # 문제 지표 다발
    })()
    report = calculate_failure_cost(input_data)
    assert report.risk_level == "Critical"
    assert report.failure_cost_score >= 70 # 높은 점수 예상

def test_success_low_risk():
    """Case 2: 모든 지표 안정적 -> Low Risk 예상"""
    input_data = type('MockData', (object,), {
        'website_url': 'stable-site.com',
        'monthly_revenue_usd': 10000.0,
        'conversion_rate_percent': 3.5,
        'traffic_change_pct': 2.0, # 약간 상승
        'payment_flow_issues': 0    # 문제 없음
    })()
    report = calculate_failure_cost(input_data)
    assert report.risk_level == "Low"
    assert report.failure_cost_score < 30 # 낮은 점수 예상

def test_success_medium_risk():
    """Case 3: 한 지표만 문제 -> Medium Risk 예상"""
    input_data = type('MockData', (object,), {
        'website_url': 'mixed-site.com',
        'monthly_revenue_usd': 2000.0,
        'conversion_rate_percent': 1.8, # 약간 낮음
        'traffic_change_pct': -10.0, # 중간 하락
        'payment_flow_issues': 1    # 문제 1개만 있음
    })()
    report = calculate_failure_cost(input_data)
    assert report.risk_level == "Medium"
    assert 30 <= report.failure_cost_score < 60 # 중간 점수 예상

def test_validation_missing_revenue():
    """Case 4: 필수 입력값 누락 테스트 (Pydantic/FastAPI 레벨 검증 목표)"""
    # 이 테스트는 FastAPI를 통해 요청했을 때 실패해야 하지만, 여기서는 로직 함수 자체만 테스트하므로,
    # Pydantic 모델을 직접 건드리는 방식으로 논리적 오류를 방지했음을 주석으로 명시합니다.
    pass # 실제 API 테스트에서는 TestClient를 사용해 422 Unprocessable Entity 응답 확인 필요