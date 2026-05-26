from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QuizSubmission(Base):
    __tablename__ = "quiz_submissions"

    # 사용자 식별 정보 (Lead Magnet 확보 목적)
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False, unique=True) # 이메일 중복 방지
    company_name = Column(String, nullable=True)

    # 진단 결과 데이터 (핵심 지표)
    total_questions = Column(Integer, default=0)
    score = Column(Float, nullable=False)  # 점수 (예: 10점 만점에 8.5점)
    tech_debt_level = Column(String, nullable=True) # 예: 'Critical', 'Moderate', 'Low'

    # 운영 데이터
    submission_timestamp = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<QuizSubmission(email='{self.user_email}', score={self.score})>"