from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from src.config import SQLALCHEMY_URL


engine = create_engine(
    SQLALCHEMY_URL,
    echo=SQLALCHEMY_URL.startswith("sqlite"),
)


class LocalSession(Session):
    pass


def get_session():
    with LocalSession(engine) as session:
        yield session


ActualSession = Annotated[LocalSession, Depends(get_session)]
