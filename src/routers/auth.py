from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from google.oauth2 import id_token
from google.auth.transport import requests
from src.config import (
    GOOGLE_CLIENT_ID,
    SWAGGER_HELPER_URL,
    ACCESS_SECRET_KEY,
    REFRESH_SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
)
from fastapi import HTTPException

from pydantic import BaseModel
from datetime import timedelta
from database.models.contacts_kvd import create_contact, ContactsKvd
from database.models.user import User, create_user, get_user_by_email, get_user_by_id
from src.services.user_profile_service import gen_default_profile
from src.utils.jwt import get_payload_from_token, create_token
from database.db import ActualSession
from database.models.auth_provider import AuthProviderRaw as AuthProvider

router = APIRouter()

oauth2_schema = HTTPBearer(
    description=f"""
#### How to get access token
1. [Sign in with Google]({SWAGGER_HELPER_URL})
2. Token from step 1 should be used in `/sign-in` endpoint
3. Access token from `/sign-in` insert into input below
""",
)


class SignIn(BaseModel):
    credential: str
    auth_provider: AuthProvider


class Refresh(BaseModel):
    refresh_token: str


def get_me(
    auth_credentials: Annotated[HTTPAuthorizationCredentials, Depends(oauth2_schema)],
    session: ActualSession,
):
    payload = get_payload_from_token(
        token=auth_credentials.credentials,
        secret=ACCESS_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    me = get_user_by_id(payload["id"], session)
    return me


Me = Annotated[User, Depends(get_me)]


@router.post("/sign-in")
def sign_in(
    body: SignIn,
    session: ActualSession,
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
def refresh(body: Refresh, session: ActualSession):
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
