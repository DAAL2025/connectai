from fastapi import APIRouter, HTTPException, status
from .schemas import AuditInputSchema, FCReportSchema

# 라우터 정의 (FastAPI 스타일)
router = APIRouter(prefix="/audit", tags=["Audit"])

@router.post("/calculate_fc", response_model=FCReportSchema, status_code=status.HTTP_200_OK)
async def calculate_failure_cost_report(input: AuditInputSchema):
    """
    사용자가 제공한 비즈니스 지표를 기반으로 재무적 손실 비용(FC)을 계산하고 상세 보고서를 반환합니다.
    [근거: CEO 지시/Self-RAG] - 모든 Funnel 백엔드에 FC 데이터 기반의 강력한 유효성 검증 및 에러 핸들링 로직 최우선 확보
    """
    try:
        # 1. 스키마를 통해 이미 입력값 검증 완료 (Pydantic 자동 처리)

        # 2. 비즈니스 로직 호출 (순수 함수 분리 원칙 준수)
        report = calculate_fc_report(input)

        return report
    except Exception as e:
        # 내부 서버 오류가 발생했을 경우를 대비한 안전장치 (Fail-Safe)
        print(f"🚨 Critical Backend Error during FC calculation: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="FC 계산 중 시스템 오류가 발생했습니다. 관리자에게 문의해주세요.")

# 📊 평가: 완료 — 핵심 데이터 스키마와 이를 사용하는 API 엔드포인트 정의를 통해 백엔드의 구조적 요구사항을 확립했기 때문에.
# 📝 다음 단계: FastAPI 서버 환경 설정 및 실제 비즈니스 로직(재무 모델링) 구현 - `schemas.py` 내의 calculate_fc_report 함수에 핵심 재무 계산 알고리즘을 이식해야 합니다.