from sqlmodel import SQLModel, Field, ForeignKey


class Language_54ccd4bc9959(SQLModel):
    __tablename__ = 'languages'
    id: int | None = Field(default=None, primary_key=True)
    language: str = Field(nullable=False)
    level: str | None
    certificate: str | None
    details: str | None
    user_id: int = Field(ForeignKey(
        'users.id', ondelete='cascade'), nullable=False)
    profile_id: int | None = Field(
        ForeignKey('profiles.id', ondelete='set null'))
