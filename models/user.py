from sqlmodel import select, Session, Relationship
from sqlalchemy import orm
from .profile import Profile, ProfileRes
from .auth_provider import AuthProvider, AuthProviderEnum
from sqlmodel import Field, SQLModel


class BaseUser(SQLModel):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    email: str | None = Field(str, unique=True)
    sub: str | None = Field(str, unique=True)
    auth: AuthProviderEnum = Field(AuthProvider)


class User(BaseUser, table=True):
    __tablename__ = "users"

    profiles: list[Profile] = Relationship(
        sa_relationship=orm.relationship(
            Profile,
            cascade='all, delete-orphan',
        ))


class UserRes(BaseUser):
    profiles: list[ProfileRes] = []


def get_user_by_email(email: str, session: Session):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    return user


def get_user_by_id(user_id: int, session: Session):
    sql_query = select(User).where(User.id == user_id)
    user = session.exec(sql_query).first()

    if not user:
        return user

    return user


def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
