from models.profile import Profile
from sqlmodel import Session, select
from models.user import User
from schemas.profile import ProfileReq


def gen_default(user: User, session: Session):
    default_profile = Profile(user_id=user.id)
    session.add(default_profile)
    session.commit()
    session.refresh(default_profile)

    return default_profile


def get(*, user_id: int, profile_name: str, session: Session):
    sql_query = select(Profile).where(
        Profile.user_id == user_id,
        Profile.name == profile_name,
    )
    profile = session.exec(sql_query).first()

    return profile


def upsert(
    *,
    user_id: int,
    data: ProfileReq,
    session: Session,
):
    profile = get(
        user_id=user_id, profile_name=data.name, session=session)

    if not profile:
        profile = Profile(
            user_id=user_id,
            name=data.name,
        )

    if data.contacts:
        for c in data.contacts:
            c.user_id = user_id
        profile.contacts = data.contacts

    if data.education:
        for ed in data.education:
            ed.user_id = user_id
        profile.education = data.education

    if data.experience:
        for exp in data.experience:
            exp.user_id = user_id
        profile.experience = data.experience

    if data.languages:
        for l in data.languages:
            l.user_id = user_id
        profile.languages = data.languages

    if data.skills:
        for s in data.skills:
            s.user_id = user_id
        profile.skills = data.skills

    if data.avatar:
        data.avatar.user_id = user_id
        profile.avatar = data.avatar

    session.add(profile)
    session.commit()
    session.refresh(profile)

    return profile
