from sqlmodel import SQLModel, Field, ForeignKey


class Skill_c5b2e6ef6c14(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    user_id: int = Field(ForeignKey(
        'users.id', ondelete='cascade'), nullable=False)
    profile_id: int | None = Field(
        ForeignKey('profiles.id', ondelete='set null'))
    details: str | None
    certificate: str | None
