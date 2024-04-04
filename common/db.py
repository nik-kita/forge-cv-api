from sqlmodel import create_engine, Session
from typing import Annotated
from fastapi import Depends
from common.config import SQLALCHEMY_URL


_engine = create_engine(
    SQLALCHEMY_URL,
    echo=True,
    connect_args={
        "check_same_thread": False,
    } if SQLALCHEMY_URL.startswith("sqlite")
    else None
)


def _get_session():
    with Session(_engine) as session:
        yield session


Db = Annotated[Session, Depends(_get_session)]
