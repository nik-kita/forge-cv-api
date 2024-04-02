from sqlmodel import Field, SQLModel, Enum
from .auth_provider_4451bbbfbdbd import AuthProvider4451bbbfbdbd


class BaseUsered2df492986b(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


AuthProvider = Enum(AuthProvider4451bbbfbdbd)


class Userced2df492986b(BaseUsered2df492986b):
    __tablename__ = "users"
    email: str | None = Field(str, unique=True, nullable=True)
    sub: str | None = Field(str, unique=True, nullable=True)
    auth_provider: AuthProvider4451bbbfbdbd = Enum(AuthProvider4451bbbfbdbd)
