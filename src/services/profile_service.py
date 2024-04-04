from models.profile_model import Profile
from sqlmodel import Session, select
from models.user_model import User
from schemas.profile_schema import ProfileReq
from fastapi import HTTPException


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


def delete(*, user_id: int, profile_id: int, session: Session):
    profile = session.get(Profile, profile_id)

    if profile is None:
        raise HTTPException(404, "Profile not found")
    elif profile.user_id != user_id:
        raise HTTPException(403, "Forbidden")

    session.delete(profile)
    session.commit()


def upsert(
    *,
    user_id: int,
    data: ProfileReq,
    session: Session,
):
    profile = get(
        user_id=user_id, profile_name=data.name, session=session
    ) or Profile(
        user_id=user_id,
        name=data.name,
    )

    profile.contacts = [
        c.pre_insert(user_id=user_id) for c in data.contacts
    ] if data.contacts else []

    profile.education = [
        ed.pre_insert(user_id=user_id) for ed in data.education
    ] if data.education else []

    profile.experience = [
        exp.pre_insert(user_id=user_id) for exp in data.experience
    ] if data.experience else []

    profile.languages = [
        l.pre_insert(user_id=user_id) for l in data.languages
    ] if data.languages else []

    profile.skills = [
        s.pre_insert(user_id=user_id) for s in data.skills
    ] if data.skills else []

    profile.avatar = data.avatar.pre_insert(
        user_id=user_id
    ) if data.avatar else None

    session.add(profile)
    session.commit()
    session.refresh(profile)

    return profile
