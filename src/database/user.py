from sqlmodel import SQLModel, Field, Session, select
from .db import engine


class BaseUser(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class User(BaseUser, table=True):
    email: str | None = Field(str, unique=True, nullable=True)
    sub: str | None = Field(str, unique=True, nullable=True)


def get_user_by_email(email: str):
    user = None
    with Session(engine) as session:
        sql_query = select(User).where(User.email == email)
        user = session.exec(sql_query).first().model_dump()

    return user


def get_user_by_id(user_id: int):
    user = None
    with Session(engine) as session:
        sql_query = select(User).where(User.id == user_id)
        user = session.exec(sql_query).first().model_dump()

    return user
