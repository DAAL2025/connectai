from fastapi import FastAPI, HTTPException
from app.schemas.mini_audit_schema import AuditInput, FailureCostReport
import random # 시뮬레이션용

app = FastAPI(title="D.AAL Mini-Audit API", description="재무적 손실 비용 측정 엔진.")

# [백엔드 핵심 로직] - 실제 데이터 과학 모델이 들어갈 자리 (현재는 Mock 구현)
def calculate_failure_cost(data: AuditInput) -> FailureCostReport:
    """
    Mini-Audit 입력 데이터를 받아 재무적 손실 비용 점수와 보고서를 도출합니다.
    [근거: CEO 지시/Self-RAG] - Mini-Audit Funnel의 핵심 로직 구현 목표.
    """
    # 1. Failure Cost Score 계산 (가중치 기반 가상 모델)
    score = 0.0

    # 매출액 변화에 따른 가중치 부여 (Traffic Drop이 가장 중요하다고 가정)
    if data.traffic_change_pct is not None and data.traffic_change_pct < -15:
        score += abs(data.traffic_change_pct) * 0.8  # 큰 하락은 높은 점수 기여
    elif data.traffic_change_pct is not None and data.traffic_change_pct < -5:
        score += abs(data.traffic_change_pct) * 0.3

    # 전환율과 문제 지표의 영향을 합산
    conversion_impact = max(0, (100 - data.conversion_rate_percent) / 20)
    payment_impact = data.payment_flow_issues * 5.0

    score += conversion_impact + payment_impact

    # 최종 점수를 0에서 100 사이로 스케일링 및 랜덤 노이즈 추가 (현실적 모의 테스트를 위해)
    failure_cost_score = min(100, max(1.0, score * 2 + random.uniform(-5, 5)))

    # 2. Risk Level 및 Suggestion 도출
    if failure_cost_score >= 80:
        risk_level = "Critical"
        suggested_action = "즉시 결제 플로우 A/B 테스트를 재설계하고 트래픽 유입 경로를 다각화해야 합니다."
    elif failure_cost_score >= 50:
        risk_level = "High"
        suggested_action = "현재 비즈니스 구조의 근본적인 문제(기술 부채, 운영 시스템) 진단이 필요합니다. Mini-Audit 컨설팅을 받으세요."
    elif failure_cost_score >= 20:
        risk_level = "Medium"
        suggested_action = "일부 지표에서 이상 징후가 포착되었습니다. 성장 로직(Growth Logic) 점검이 필요합니다."
    else:
        risk_level = "Low"
        suggested_action = "현재 시스템은 안정적입니다. 다음 성장을 위한 예측 모델 구축에 집중하세요."

    # 3. 상세 분석 데이터 구성
    detailed_analysis = {
        "traffic_assessment": f"{data.traffic_change_pct:.1f}% 변화율에 따른 위험도.",
        "conversion_assessment": f"{data.conversion_rate_percent:.1f}% 전환율은 목표 대비 어느 수준인가요?",
        "payment_flow_alert": f"총 {data.payment_flow_issues}개의 결제 플로우 문제 지표가 감지되었습니다."
    }

    return FailureCostReport(
        failure_cost_score=round(failure_cost_score, 2),
        risk_level=risk_level,
        suggested_action=suggested_action,
        detailed_analysis=detailed_analysis
    )


@app.post("/api/v1/mini-audit/calculate", response_model=FailureCostReport)
async def run_mini_audit(input_data: AuditInput):
    """Mini-Audit Funnel의 최종 실패 비용 측정 API 엔드포인트입니다."""
    try:
        # 입력값 유효성 검증은 Pydantic과 FastAPI 레벨에서 이미 처리됩니다.
        report = calculate_failure_cost(input_data)
        return report
    except Exception as e:
        # 백엔드 예외 포착 및 로깅 (실제 운영 환경에서는 더 정교한 로깅 필요)
        print(f"Error during mini-audit calculation: {e}")
        raise HTTPException(status_code=500, detail="Mini-Audit 계산 중 내부 서버 오류가 발생했습니다.")