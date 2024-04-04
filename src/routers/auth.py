from fastapi import APIRouter
from google.oauth2 import id_token
from google.auth.transport import requests
from common.config import (
    GOOGLE_CLIENT_ID,
    REFRESH_SECRET_KEY,
    ALGORITHM,
)
from fastapi import HTTPException
from models.contacts_kvd import create_contact, ContactsKvd
from models.user import User, create_user, get_user_by_email, get_user_by_id
from schemas.auth import Refresh, SignIn
from src.services.auth import JwtTypeEnum, gen_jwt_res
from src.services.profile import gen_default
from utils.jwt import get_payload_from_token
from common.db import Db

router = APIRouter()


@router.post("/sign-in")
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

    user = get_user_by_email(data["email"], session)

    if not user:
        user = create_user(
            User(email=data["email"], sub=data["sub"],
                 auth=body.auth_provider), session
        )
        profile = gen_default(user=user, session=session)

        if user.email:
            create_contact(contact=ContactsKvd(
                profile_id=profile.id,
                user_id=user.id,
                key="email",
                value=user.email,
            ), session=session)

    res = gen_jwt_res(user_id=user.id, jwt_type=JwtTypeEnum.ACCESS)

    return res


@router.post("/refresh")
def refresh(body: Refresh, session: Db):
    payload = get_payload_from_token(
        token=body.refresh_token,
        secret=REFRESH_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    user = get_user_by_id(payload["id"], session=session)

    if user is None:
        raise HTTPException(401, "Invalid token")

    res = gen_jwt_res(user_id=user.id, jwt_type=JwtTypeEnum.REFRESH)

    return res
