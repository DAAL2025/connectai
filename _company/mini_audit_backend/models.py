class AuditLog(BaseModel):
    """시스템의 모든 중요 상호작용 및 데이터 변경 이력을 추적하는 모델."""
    log_id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: int = Field(index=True, description="액션을 수행한 사용자 ID")
    entity_type: str = Field(description="영향을 받은 엔티티 타입 (예: 'MiniAuditResult', 'Payment')")
    entity_id: UUID = Field(description="수정된 또는 생성된 엔티티의 ID")
    action: str = Field(description="발생한 액션 종류 (예: 'DATA_INPUT', 'COST_CALCULATION', 'STATUS_UPDATE')")
    details: JSON = Field(description="상세 변경 내용 (변경 전/후 값 또는 관련 데이터)")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    performed_by: str = Field(description="액션을 수행한 주체 (예: 'User', 'System Script')")

# 참고: 이 모델은 별도의 테이블로 관리되어야 하며, ORM 레벨에서 트랜잭션 커밋 시점에 기록됩니다.