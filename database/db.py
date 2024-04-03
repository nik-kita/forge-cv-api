from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from src.config import SQLALCHEMY_URL


engine = create_engine(
    SQLALCHEMY_URL,
    echo=True,
    connect_args={
        "check_same_thread": False,
    } if SQLALCHEMY_URL.startswith("sqlite")
    else None
)


def get_session():
    with Session(engine) as session:
        yield session


ActualSession = Annotated[Session, Depends(get_session)]
