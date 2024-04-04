from models.user import User
from sqlmodel import Session, select


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
