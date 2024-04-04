from sqlmodel import Relationship
from sqlalchemy import orm

from .profile_model import Profile
from .auth_provider_enum import AuthProvider, AuthProviderEnum
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    email: str | None = Field(str, unique=True)
    sub: str | None = Field(str, unique=True)
    auth: AuthProviderEnum = Field(AuthProvider)

    profiles: list[Profile] = Relationship(
        sa_relationship=orm.relationship(
            Profile,
            cascade='all, delete-orphan',
        ))
