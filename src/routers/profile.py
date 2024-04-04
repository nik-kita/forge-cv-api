from fastapi import APIRouter
from common.db import Db
from common.auth import Me_and_Session
from src.services.user_profile_service import UpsertProfile, get_user_profile, upsert_profile

router = APIRouter()


@router.get('/{name}')
def get_profile_by_name(name: str, me_and_session: Me_and_Session):
    me, session = me_and_session
    res = get_user_profile(user_id=me.id, profile_name=name, session=session)

    return res


@router.post('/{name}')
def upsert_profile_by_name(
    name: str,
    me_and_session: Me_and_Session,
    session: Db,
    data: UpsertProfile,
):
    me, session = me_and_session
    res = upsert_profile(
        profile_name=name,
        user_id=me.id,
        data=data,
        session=session,
    )

    return res
