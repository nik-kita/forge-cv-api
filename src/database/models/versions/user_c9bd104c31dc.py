from sqlmodel import SQLModel, Field


class BaseUserc9bd104c31dc(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class Userc9bd104c31dc(BaseUserc9bd104c31dc, table=True):
    __tablename__ = "users"

    email: str | None = Field(str, unique=True, nullable=True)
    sub: str | None = Field(str, unique=True, nullable=True)
