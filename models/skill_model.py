from sqlmodel import SQLModel, Field


class Skill(SQLModel, table=True):
    __tablename__ = "skills"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    user_id: int = Field(nullable=False, foreign_key='users.id')
    profile_id: int | None = Field(foreign_key='profiles.id')
    details: str | None
    certificate: str | None
