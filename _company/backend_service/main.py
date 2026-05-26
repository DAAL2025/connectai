from fastapi import FastAPI, HTTPException, status
from pydantic import ValidationError
from fc_service import FinancialLossCost, calculate_fc, FCResult

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="D.AAL DESIGN - FC Prediction API",
    description="클라이언트의 재무적 손실 비용(FC)을 계산하고 경고 레벨을 제공하는 핵심 백엔드 서비스.",
    version="1.0.0"
)

@app.post("/api/calculate-fc", response_model=FCResult, summary="재무적 손실 비용 예측 및 위기 진단")
async def calculate_fc_endpoint(data: FinancialLossCost):
    """
    POST /api/calculate-fc
    클라이언트가 제공한 재무 데이터를 기반으로 $FC$를 계산하고 
    위험 레벨(Normal, Warning, Crisis)을 판단합니다.

    Args:
        data: 요청 본문 (FinancialLossCost 모델 준수 필요).
    
    Returns:
        FCResult: 예측된 FC 값과 최종 경고 상태가 담긴 객체.
    """
    try:
        # 1. 데이터 유효성 검증은 FastAPI/Pydantic에 의해 자동 처리됩니다. (data 변수로 접근 가능)
        # 2. 비즈니스 로직 호출 및 실행
        result = calculate_fc(data)
        return result

    except Exception as e:
        # 예측 엔진 자체의 내부 오류 또는 시스템 오류 처리
        print(f"Critical Error during FC calculation: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="재무 분석 서비스에 일시적인 문제가 발생했습니다. 잠시 후 다시 시도해 주세요."
        )

# 서버 실행 명령어 (실제 사용자가 이해하기 쉽도록 주석 처리)
# To run: uvicorn backend_service.main:app --reload