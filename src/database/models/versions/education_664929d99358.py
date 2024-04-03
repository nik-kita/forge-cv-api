from sqlmodel import SQLModel, Field


class Education_664929d99358(SQLModel):
    __tablename__ = 'educations'
    id: int | None = Field(default=None, primary_key=True)
    from_date: str | None
    to_date: str | None
    diploma: str | None
    certificate: str | None
    details: str | None
    education: str | None
    university: str = Field(nullable=False)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    profile_id: int | None = Field(foreign_key='profiles.id')
    degree: str | None
