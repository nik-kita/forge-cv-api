from sqlmodel import SQLModel, Field


class Contact(SQLModel, table=True):
    __tablename__ = "contacts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    profile_id: int | None = Field(foreign_key='profiles.id')
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    details: str | None = None
