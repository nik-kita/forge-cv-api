from fastapi import APIRouter, Body
from typing import Annotated
from database.db import ActualSession
from src.routers.auth import Me
from src.services.user_profile_service import UpsertProfile, get_user_profile, upsert_profile

router = APIRouter()


@router.get('/{name}')
def get_profile_by_name(name: str, me: Me, session: ActualSession):
    res = get_user_profile(user_id=me.id, profile_name=name, session=session)

    return res


@router.post('/{name}')
def upsert_profile_by_name(
    name: str,
    me: Me,
    session: ActualSession,
    data: UpsertProfile,
):
    res = upsert_profile(
        profile_name=name,
        user_id=me.id,
        data=data,
        session=session,
    )

    return res
