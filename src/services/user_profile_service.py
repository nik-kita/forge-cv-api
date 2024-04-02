from src.database.models.profile import Profile
from sqlmodel import Session
from src.database.models.user import User


def gen_default_profile(user: User, session: Session):
    default_profile = Profile(user_id=user.id)
    session.add(default_profile)
    session.commit()
    session.refresh(default_profile)

    return default_profile
