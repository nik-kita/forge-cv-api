from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


class LocalSession(Session):
    pass


def get_session():
    with LocalSession(engine) as session:
        yield session


ActualSession = Annotated[LocalSession, Depends(get_session)]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

