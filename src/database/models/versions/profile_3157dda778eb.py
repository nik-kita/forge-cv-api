from sqlmodel import SQLModel, Field


class Profile_3157dda778eb(SQLModel):
    __tablename__ = "profiles"
    user_id: int = Field(foreign_key='users.id', nullable=False)
    avatar_id: int | None = Field(foreign_key='avatars.id')
    summary: str | None
    name: str | None = Field(default='default')
    details: str | None
    id: int | None = Field(default=None, primary_key=True)
