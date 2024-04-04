from sqlmodel import SQLModel, Field


class BaseAvatar(SQLModel):
    __tablename__ = "avatars"
    id: int | None = Field(default=None, primary_key=True)
    link: str = Field(nullable=False)
    name: str | None
    details: str | None
    user_id: int = Field(foreign_key='users.id', nullable=False)


class Avatar(BaseAvatar, table=True):
    __tablename__ = "avatars"
