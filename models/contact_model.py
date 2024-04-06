from sqlmodel import SQLModel, Field


class Contact(SQLModel, table=True):
    __tablename__ = "contacts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    details: str | None = None
