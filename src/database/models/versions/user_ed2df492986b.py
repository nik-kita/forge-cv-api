from sqlmodel import Field, SQLModel, Enum
from .auth_provider_4451bbbfbdbd import AuthProvider4451bbbfbdbd


AuthProvider = Enum(AuthProvider4451bbbfbdbd)


class Userced2df492986b(SQLModel):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    email: str | None = Field(str, unique=True)
    sub: str | None = Field(str, unique=True)
    auth: AuthProvider4451bbbfbdbd = Enum(AuthProvider4451bbbfbdbd)
