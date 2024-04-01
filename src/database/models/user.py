from sqlmodel import select, Session
from .versions.user_c9bd104c31dc import Userc9bd104c31dc, BaseUserc9bd104c31dc

BaseUser = BaseUserc9bd104c31dc
User = Userc9bd104c31dc

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
