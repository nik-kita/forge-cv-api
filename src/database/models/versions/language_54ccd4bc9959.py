from sqlmodel import SQLModel, Field


class Language_54ccd4bc9959(SQLModel):
    __tablename__ = 'languages'
    id: int | None = Field(default=None, primary_key=True)
    language: str = Field(nullable=False)
    level: str | None
    certificate: str | None
    details: str | None
    user_id: int = Field(foreign_key='users.id', nullable=False)
    profile_id: int | None = Field(foreign_key='profiles.id')
