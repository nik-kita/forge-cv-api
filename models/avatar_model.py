from sqlmodel import SQLModel, Field


class Avatar(SQLModel, table=True):
    __tablename__ = "avatars"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    link: str = Field(nullable=False)
    name: str | None
    details: str | None
