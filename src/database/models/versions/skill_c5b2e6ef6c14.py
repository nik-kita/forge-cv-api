from sqlmodel import SQLModel, Field


class Skill_c5b2e6ef6c14(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    user_id: int = Field(nullable=False, foreign_key='users.id')
    profile_id: int | None = Field(foreign_key='profiles.id')
    details: str | None
    certificate: str | None
