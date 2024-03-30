from sqlmodel import SQLModel, Field, select
from .db import LocalSession


class BaseUser(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class User(BaseUser, table=True):
    __tablename__ = "users"

    email: str | None = Field(str, unique=True, nullable=True)
    sub: str | None = Field(str, unique=True, nullable=True)


def get_user_by_email(email: str, session: LocalSession):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    return user


def get_user_by_id(user_id: int, session: LocalSession):
    sql_query = select(User).where(User.id == user_id)
    print(sql_query)
    user = session.exec(sql_query).first()

    return user


def create_user(user: User, session: LocalSession):
    session.add(user)
    session.commit()
    session.refresh(user)
    print(user)

    return user
