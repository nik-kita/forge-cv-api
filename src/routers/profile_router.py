from fastapi import APIRouter, Response, status
from common.db import Db
from common.auth import Me_and_Session
from src.services import profile_service
from schemas.profile_schema import ProfileRes, ProfileReq


profile_router = APIRouter()


@profile_router.get('/{name}')
def get_profile_by_name(name: str, me_and_session: Me_and_Session) -> ProfileRes | None:
    me, session = me_and_session
    res = profile_service.get(
        user_id=me.id, profile_name=name, session=session)

    return res


@profile_router.post('/')
def upsert_profile(
    me_and_session: Me_and_Session,
    session: Db,
    data: ProfileReq,
) -> ProfileRes:
    me, session = me_and_session
    res = profile_service.upsert(
        user_id=me.id,
        data=data,
        session=session,
    )

    return res


@profile_router.delete('/{profile_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_profile(profile_id: int, me_and_session: Me_and_Session):
    me, session = me_and_session
    profile_service.delete(
        user_id=me.id,
        profile_id=profile_id,
        session=session,
    )
