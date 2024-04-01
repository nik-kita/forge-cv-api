from sqlmodel import SQLModel, Field, select, Session
from .versions.user_b572a6280767 import User as VersionedUser

User = VersionedUser


def get_user_by_email(email: str, session: Session):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    return user


def get_user_by_id(user_id: int, session: Session):
    sql_query = select(User).where(User.id == user_id)
    user = session.exec(sql_query).first()

    return user


def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
