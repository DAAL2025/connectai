from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from src.db.schema import QuizSubmission # Step 1에서 정의한 스키마 임포트
# from sqlalchemy.orm import Session # 실제 DB 세션 객체 가정

router = APIRouter()

# 클라이언트로부터 받을 데이터의 구조 정의 (Pydantic Schema)
class QuizInput(BaseModel):
    email: EmailStr = Field(..., description="사용자 이메일 주소")
    company_name: str | None = Field(None, description="회사 이름 (선택사항)")
    score: float = Field(..., gt=0, le=10, description="진단 점수 (0.0 ~ 10.0)")
    tech_debt_level: str = Field(..., pattern="^(Critical|Moderate|Low)$", description="기술 부채 레벨")

@router.post("/submit", status_code=status.HTTP_201_CREATED)
async def submit_quiz_score(data: QuizInput):
    """
    자가진단 툴 결과를 받아 DB에 기록하고, 성공적으로 처리했음을 응답합니다.
    [검증 필요] 이메일 중복 체크 및 트랜잭션 처리가 핵심입니다.
    """
    try:
        # 1. 유효성 검사 (Pydantic이 이미 했지만, 비즈니스 로직 재확인)
        if data.score < 0 or data.score > 10:
            raise ValueError("점수는 반드시 0점에서 10점 사이여야 합니다.")

        # 2. DB 트랜잭션 시작 (실제 DB 세션을 사용한다고 가정)
        # db_session = SessionLocal()
        # try:
        #     submission = QuizSubmission(
        #         user_email=data.email,
        #         company_name=data.company_name,
        #         score=data.score,
        #         tech_debt_level=data.tech_debt_level # DB 스키마와 맞춰서 저장
        #     )
        #     db_session.add(submission)
        #     db_session.commit()
        #     return {"message": "진단 결과가 성공적으로 기록되었습니다.", "success": True}
        # except Exception as e:
        #     db_session.rollback()
        #     raise HTTPException(status_code=400, detail=f"데이터 저장 실패: {str(e)}")

        # [현재는 Mocking하여 성공 응답만 반환]
        print(f"✅ Mock DB Save Success: Email={data.email}, Score={data.score}")
        return {"message": "진단 결과가 성공적으로 기록되었습니다.", "success": True}

    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="서버 내부 오류 발생")