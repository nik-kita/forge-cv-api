from sqlmodel import SQLModel, Field, ForeignKey


class Profile_3157dda778eb(SQLModel):
    __tablename__ = "profiles"
    user_id: int = Field(ForeignKey(
        "users.id", ondelete='cascade'), nullable=False)
    avatar_id: int | None = Field(
        ForeignKey("avatars.id", ondelete='set null'))
    summary: str | None
    name: str | None = Field(default='default')
    details: str | None
    id: int | None = Field(default=None, primary_key=True)
