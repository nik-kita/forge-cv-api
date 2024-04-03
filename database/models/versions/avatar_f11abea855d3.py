from sqlmodel import SQLModel, Field


class Avatar_f11abea855d3(SQLModel):
    __tablename__ = "avatars"
    id: int | None = Field(default=None, primary_key=True)
    link: str = Field(nullable=False)
    name: str | None
    details: str | None
    user_id: int = Field(foreign_key='users.id', nullable=False)
