from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from fastapi.responses import JSONResponse
from common.auth import Me_and_Session
from common.db import Db
from models.contact_model import Contact
from models.education_model import Education
from models.experience_model import Experience
from models.language_model import Language
from models.skill_model import Skill
from schemas.exception_400_schema import Exception_400
from schemas.user_schema import PublicUserRes
from src.services import user_service

user_router = APIRouter()


target_model = {
    "contacts": Contact,
    "educations": Education,
    "experiences": Experience,
    "languages": Language,
    "skills": Skill,
}


def only_target(canditate: str):
    if canditate not in target_model:
        raise HTTPException(400, detail=f"""\
use one from {[k for k in target_model.keys()]}""")

    return canditate


@user_router.get('/my/{target}')
def my(me_and_session: Me_and_Session, target: Annotated[str, Depends(only_target)]):
    me, session = me_and_session
    result = user_service.all_my(me.id, target_model[target], session)

    return result


@user_router.put('/nik/{nik}', responses={400: {"model": Exception_400}})
def modify_nik(nik: str, me_and_session: Me_and_Session) -> PublicUserRes:
    me, session = me_and_session
    (success, user_or_fail_reason) = user_service.modify(
        user_id=me.id, session=session, nik=nik)

    if not success:
        return JSONResponse(status_code=400, content=Exception_400(message=user_or_fail_reason).model_dump())

    return user_or_fail_reason


@user_router.delete('/nik', status_code=204)
def rm_nik(me_and_session: Me_and_Session) -> None:
    me, session = me_and_session
    user_service.modify(user_id=me.id, session=session)

    return None


@user_router.get('/{nik}', tags=['public'])
def get_public_by_nik(nik: str, session: Db) -> PublicUserRes:
    user = user_service.get_public_by_nik(nik, session)

    if not user:
        raise HTTPException(404, f"User {nik} was not found")

    return user
