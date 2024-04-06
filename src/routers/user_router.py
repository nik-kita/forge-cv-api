from fastapi import APIRouter

from common.auth import Me_and_Session
from models.skill_model import Skill
from src.services import user_service

user_router = APIRouter()


@user_router.get('/skills')
def my_skills(me_and_session: Me_and_Session):
    me, session = me_and_session
    result = user_service.all_my(me.id, Skill, session)

    print(result)

    return result
