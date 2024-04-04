from fastapi import APIRouter
from common.db import Db
from common.auth import Me_and_Session
from src.services import profile
from schemas.profile import UpsertProfileRes, UpsertProfile
router = APIRouter()


@router.get('/{name}')
def get_profile_by_name(name: str, me_and_session: Me_and_Session):
    me, session = me_and_session
    res = profile.get(user_id=me.id, profile_name=name, session=session)

    return res


@router.post('/', response_model=UpsertProfileRes)
def upsert_profile(
    me_and_session: Me_and_Session,
    session: Db,
    data: UpsertProfile,
):
    me, session = me_and_session
    res = profile.upsert(
        user_id=me.id,
        data=data,
        session=session,
    )

    return res
