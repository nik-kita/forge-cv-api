from sqlmodel import select, Session, Relationship
from sqlalchemy import orm
from .versions.user_ed2df492986b import Userced2df492986b
from .profile import Profile, ProfileRes


BaseUser = Userced2df492986b


class User(Userced2df492986b, table=True):
    __tablename__ = "users"

    profiles: list[Profile] = Relationship(
        sa_relationship=orm.relationship(
            Profile,
            cascade='all, delete-orphan',
        ))


class UserRes(BaseUser):
    profiles: list[ProfileRes] = []


def get_user_by_email(email: str, session: Session):
    sql_query = select(User).where(User.email == email)
    user = session.exec(sql_query).first()

    user and print(user.profiles)

    return user


def get_user_by_id(user_id: int, session: Session):
    sql_query = select(User).where(User.id == user_id)
    user = session.exec(sql_query).first()

    if not user:
        return user

    print()
    print(user.profiles)
    print()

    return user


def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
