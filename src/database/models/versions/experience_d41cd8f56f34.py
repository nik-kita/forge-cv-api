from sqlmodel import SQLModel, Field, ForeignKey

class Experience_d41cd8f56f34(SQLModel):
    __tablename__ = 'experiences'
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(ForeignKey('users.id', ondelete='cascade'), nullable=False)
    profile_id: int | None = Field(ForeignKey('profiles.id', ondelete='set null'))
    company: str = Field(nullable=False)
    from_date: str | None
    to_date: str | None
    duration: str | None
    details: str | None
    position: str | None
    certificate: str | None
    reference_letter: str | None
