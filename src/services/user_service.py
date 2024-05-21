from fastapi import HTTPException
from models.user_model import User
from sqlmodel import SQLModel, Session, select


def get_by_email(email: str, session: Session):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    return user


def get_by_id(user_id: int, session: Session):
    sql_query = select(User).where(User.id == user_id)
    user = session.exec(sql_query).first()

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


# TODO only public info
def get_public_by_nik(nik: str, session: Session):
    sql_query = select(User).where(User.nik == nik)
    user = session.exec(sql_query).first()

    return user


def is_nik_free(*, nik: str, session: Session):
    sql_query = select(User).where(User.nik == nik)
    user = session.exec(sql_query).first()

    return user is None


def modify(
    *,
    user_id: int,
    session: Session,
    nik: str | None = None,
):
    user = get_by_id(user_id, session)

    if not user:
        return (False, "User not found")

    if nik:
        if nik == user.nik:
            return (False, "User already has that nik")
        elif not is_nik_free(nik=nik, session=session):
            return (False, f"The '{nik}' nik is already taken")
    
    user.nik = nik

    session.add(user)
    session.commit()
    session.refresh(user)

    return (True, user)
