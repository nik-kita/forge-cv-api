from fastapi import APIRouter

from src.database.db import ActualSession
from src.routers.auth import Me
from src.services.user_profile_service import get_user_profile

router = APIRouter()


@router.get('/{name}')
def get_profile_by_name(name: str, me: Me, session: ActualSession):
    res = get_user_profile(user_id=me.id, profile_name=name, session=session)

    return res
