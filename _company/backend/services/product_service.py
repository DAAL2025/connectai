from pydantic import BaseModel, ValidationError
from typing import List
from .schemas import DiagnosticInput, TierComparison, ComparisonResult, Severity

def calculate_comparison(data: DiagnosticInput) -> ComparisonResult:
    """
    진단 결과($FC$)를 분석하여 가장 적합한 제품 비교 데이터를 계산하고 반환합니다.
    이 함수는 서비스의 핵심 비즈니스 로직입니다.
    """
    total_fc = data.total_fc_estimate # $X,XXX만원

    # --- 1. 리스크 레벨 정의 및 추천 로직 결정 ---
    recommendation: str
    if total_fc >= 2000.0:  # 매우 높은 위험 (예: 월 $3000 이상)
        recommendation = "Enterprise System ($500만원)" # 최고 등급 유도
    elif total_fc >= 800.0: # 중간~높은 위험 (예: 월 $1200 ~ $3000)
        recommendation = "Growth Engine Pro ($250만원)" # 목표 등급 유도
    else:
        recommendation = "Starter Kit ($50만원)" # 기본 등급 유지

    # --- 2. 티어별 데이터 정의 및 조정 (The Core Logic) ---
    # 이 가격과 기능은 '예측 손실 비용 대비 가치'를 기준으로 재조정됩니다.

    tiers: List[TierComparison] = [
        # Tier A: Starter Kit - 최소한의 방어선
        TierComparison(
            tier_name="Starter Kit",
            price_usd=500000, # 50만원
            is_recommended=(recommendation == "Starter Kit ($50만원)"),
            feature_list=["기본 구조 검토 (Audit)", "패닉 방지 가이드라인 제공"],
            fc_mitigation_potential=0.2 # 리스크 완화 효과 낮음
        ),
        # Tier B: Growth Engine Pro - 권장 시스템 (Default Recommendation)
        TierComparison(
            tier_name="Growth Engine Pro",
            price_usd=2500000, # 250만원
            is_recommended=(recommendation == "Growth Engine Pro ($250만원)") or recommendation is None,
            feature_list=["실시간 $FC$ 추적 시스템", "구조적 결함 자동 보고서 생성", "A/B 테스트 로직 설계"],
            fc_mitigation_potential=0.6 # 가장 높은 효율성을 가진다고 가정
        ),
        # Tier C: Enterprise System - 완벽 대비책 (Max Protection)
        TierComparison(
            tier_name="Enterprise System",
            price_usd=5000000, # 500만원
            is_recommended=(recommendation == "Enterprise System ($500만원)"),
            feature_list=["AI 기반 예측 모델링 (MRR)", "전담 엔지니어 상주", "완벽한 구조적 리스크 Zero화"],
            fc_mitigation_potential=1.0 # 완벽 대비책임을 강조
        ),
    ]

    return ComparisonResult(status="success", comparison_data=tiers)


async def get_product_comparison_endpoint(data: DiagnosticInput):
    """FastAPI 라우터에서 호출될 비동기 함수 (실제 API 핸들러 역할)."""
    try:
        # 1. 데이터 유효성 검사 통과 확인 (Pydantic 덕분에 이미 처리됨)
        # 2. 핵심 로직 실행
        result = calculate_comparison(data)
        return result
    except Exception as e:
        print(f"🚨 Critical Error during comparison calculation: {e}")
        raise ValueError("Internal server error during product comparison.")