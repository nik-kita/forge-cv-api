from sqlmodel import SQLModel, Field, select, Session


class BaseUser(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class User(BaseUser, table=True):
    __tablename__ = "users"

    email: str | None = Field(str, unique=True, nullable=True)
    sub: str | None = Field(str, unique=True, nullable=True)
