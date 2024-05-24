from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from common.auth import Me_and_Session, MeOptional_and_Session
from schemas.exception_400_schema import Exception_400
from src.services import profile_service
from schemas.profile_schema import ModifyProfileReq, PaginatedRes, ProfileRes, ProfileReq
from src.services import user_service

profile_router = APIRouter()


@profile_router.get('/{nik}/{profile_name}', responses={400: {"model": Exception_400}})
def get_profile_by_name(nik: str, profile_name: str, me_and_session: MeOptional_and_Session):
    me, session = me_and_session

    if me.nik == nik:
        res = profile_service.get(
            user_id=me.id, profile_name=profile_name, session=session)

        return res

    user = user_service.get_by_nik(user_nik=nik, session=session)

    if not user:
        return JSONResponse(status_code=400, content=Exception_400(message=f"User '{nik}' not found").model_dump())

    res = profile_service.get(
        user_id=user.id, profile_name=profile_name, session=session)

    return res


@profile_router.get('/{profile_name_or_nik}')
# for user get 1 profile by name
# for guest get all (user by nik)'s profiles
def get_1_profile_by_name_or_many_of_user_by_nik(profile_name_or_nik: str, me_and_session: MeOptional_and_Session) -> PaginatedRes[ProfileRes] | ProfileRes | None:
    me, session = me_and_session

    if not me:
        nik = profile_name_or_nik
        res = profile_service.get_all_public(nik=nik, session=session)

        return res

    else:
        profile_name = profile_name_or_nik
        res = profile_service.get(
            user_id=me.id, profile_name=profile_name, session=session)

        return res


@profile_router.get('/')
# get all own profiles
def get_all_profiles(me_and_session: Me_and_Session) -> PaginatedRes[ProfileRes]:
    me, session = me_and_session
    res = profile_service.get_all_own(user_id=me.id, session=session)

    return res


@profile_router.post('/')
def upsert_profile(
    me_and_session: Me_and_Session,
    data: ProfileReq,
) -> ProfileRes:
    me, session = me_and_session
    res = profile_service.upsert(
        user_id=me.id,
        data=data,
        session=session,
    )

    return res


@profile_router.patch('/{profile_id}')
def modify_profile(
    profile_id: int,
    me_and_session: Me_and_Session,
    data: ModifyProfileReq,
) -> ProfileRes:
    me, session = me_and_session
    res = profile_service.modify(
        user_id=me.id,
        profile_id=profile_id,
        session=session,
        data=data,
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
