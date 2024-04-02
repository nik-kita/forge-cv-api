from sqlmodel import SQLModel, Field, ForeignKey


class Avatar_f11abea855d3(SQLModel):
    __tablename__ = "avatars"
    id: int | None = Field(default=None, primary_key=True)
    link: str = Field(str, nullable=False)
    name: str | None
    details: str | None
    user_id: int = Field(ForeignKey('users.id', ondelete='cascade'), nullable=False)
