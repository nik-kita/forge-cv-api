from sqlmodel import SQLModel, Field


class Avatar_f11abea855d3(SQLModel):
    __tablename__ = "avatars"
    id: int | None = Field(default=None, primary_key=True)
    link: str = Field(str, nullable=False)
    name: str = Field(str)
    details: str = Field(str)
    user_id: int = Field(int, foreign_key="users.id")
