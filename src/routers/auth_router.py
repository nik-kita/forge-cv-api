from fastapi import APIRouter
from google.oauth2 import id_token
from google.auth.transport import requests
from common.config import (
    GOOGLE_CLIENT_ID,
    REFRESH_SECRET_KEY,
    ALGORITHM,
)
from fastapi import HTTPException
from models.contact_model import Contact
from models.user_model import User
from schemas.auth_schema import Refresh, SignIn
from src.services import auth_service, user_service, profile_service, contact_service
from utils import jwt_util
from common.db import Db

auth_router = APIRouter()


@auth_router.post("/sign-in")
def sign_in(
    body: SignIn,
    session: Db,
):
    data = None
    try:
        data = id_token.verify_oauth2_token(
            body.credential, requests.Request(), GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise HTTPException(401, "Invalid token")

    user = user.get_by_email(data["email"], session)

    if not user:
        user = user_service.create(
            User(email=data["email"], sub=data["sub"],
                 auth=body.auth_provider), session
        )
        profile = profile_service.gen_default(user=user, session=session)

        if user.email:
            contact_service.create(contact=Contact(
                profile_id=profile.id,
                user_id=user.id,
                key="email",
                value=user.email,
            ), session=session)

    res = auth_service.gen_jwt_res(
        user_id=user.id, jwt_type=auth_service.JwtTypeEnum.ACCESS)

    return res


@auth_router.post("/refresh")
def refresh(body: Refresh, session: Db):
    payload = jwt_util.get_payload_from_token(
        token=body.refresh_token,
        secret=REFRESH_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    user = user_service.get_by_id(payload["id"], session=session)

    if user is None:
        raise HTTPException(401, "Invalid token")

    res = auth_service.gen_jwt_res(
        user_id=user.id, jwt_type=auth_service.JwtTypeEnum.REFRESH)

    return res
