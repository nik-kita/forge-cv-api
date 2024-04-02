from sqlmodel import SQLModel, Field, ForeignKey


class Education_664929d99358(SQLModel):
    __tablename__ = 'educations'
    id: int | None = Field(default=None, primary_key=True)
    from_date: str | None
    to_date: str | None
    diploma: str | None
    certificate: str | None
    details: str | None
    education: str | None
    university: str = Field(nullable=False)
    user_id: int = Field(ForeignKey(
        'users.id', ondelete='cascade'), nullable=False)
    profile_id: int | None = Field(
        ForeignKey('profiles.id', ondelete='set null'))
    degree: str | None