from fastapi import APIRouter
from google.oauth2 import id_token
from google.auth.transport import requests
from common.config import (
    GOOGLE_CLIENT_ID,
    ACCESS_SECRET_KEY,
    REFRESH_SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
)
from fastapi import HTTPException

from pydantic import BaseModel
from datetime import timedelta
from models.contacts_kvd import create_contact, ContactsKvd
from models.user import User, create_user, get_user_by_email, get_user_by_id
from src.services.user_profile_service import gen_default_profile
from utils.jwt import get_payload_from_token, create_token
from common.db import Db
from models.auth_provider import AuthProviderEnum

router = APIRouter()


class SignIn(BaseModel):
    credential: str
    auth_provider: AuthProviderEnum


class Refresh(BaseModel):
    refresh_token: str


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
        profile = gen_default_profile(user=user, session=session)

        if user.email:
            create_contact(contact=ContactsKvd(
                profile_id=profile.id,
                user_id=user.id,
                key="email",
                value=user.email,
            ), session=session)
    data = {
        "id": user.id,
    }
    access_token = create_token(
        data=data,
        secret=ACCESS_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = create_token(
        data=data,
        secret=REFRESH_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


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

    data = {
        "id": user.id,
    }
    access_token = create_token(
        data=data,
        secret=ACCESS_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = create_token(
        data=data,
        secret=REFRESH_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
