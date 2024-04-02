from sqlmodel import SQLModel, Field, ForeignKey


class ContactsKvd_55b11bb23614(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(ForeignKey(
        'users.id', ondelete='cascade'), nullable=False)
    profile_id: int | None = Field(
        ForeignKey('profiles.id', ondelete='set null'))
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    details: str | None
