from models.user_model import User
from sqlmodel import SQLModel, Session, select


def get_by_email(email: str, session: Session):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    return user


def get_by_id(user_id: int, session: Session):
    sql_query = select(User).where(User.id == user_id)
    user = session.exec(sql_query).first()

    if not user:
        return user

    return user


def create(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def all_my(user_id: int, target: SQLModel, session: Session):
    sql_q = select(target).where(target.user_id == user_id)
    result = session.exec(sql_q).all()

    return result
