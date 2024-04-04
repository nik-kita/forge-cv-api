from fastapi import APIRouter
from common.db import Db
from common.auth import Me_and_Session
from src.services import profile_service
from schemas.profile import ProfileRes, ProfileReq


profile_router = APIRouter()


@profile_router.get('/{name}')
def get_profile_by_name(name: str, me_and_session: Me_and_Session):
    me, session = me_and_session
    res = profile_service.get(
        user_id=me.id, profile_name=name, session=session)

    return res


@profile_router.post('/', response_model=ProfileRes)
def upsert_profile(
    me_and_session: Me_and_Session,
    session: Db,
    data: ProfileReq,
):
    me, session = me_and_session
    res = profile_service.upsert(
        user_id=me.id,
        data=data,
        session=session,
    )

    return res
