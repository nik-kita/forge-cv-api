from sqlmodel import SQLModel, Field


class Experience(SQLModel, table=True):
    __tablename__ = "experiences"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    profile_id: int | None = Field(foreign_key='profiles.id')
    company: str = Field(nullable=False)
    from_date: str | None
    to_date: str | None
    duration: str | None
    details: str | None
    position: str | None
    certificate: str | None
    reference_letter: str | None
