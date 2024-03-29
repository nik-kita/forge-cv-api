from fastapi import APIRouter
from fastapi.security import (
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
from sqlmodel import Session, select
from src.database.user import User, get_user_by_id
from src.utils.jwt import get_payload_from_token, create_token
from src.database.db import engine


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


class Refresh(BaseModel):
    refresh_token: str


@router.post("/sign-in")
def sign_in(body: SignIn):
    try:
        data = id_token.verify_oauth2_token(
            body.credential, requests.Request(), GOOGLE_CLIENT_ID
        )

        user = User(sub=data["sub"], email=data["email"])

        with Session(engine) as session:
            prev_user = session.exec(
                select(User).where(User.email == user.email)
            ).first()

            if prev_user is None:
                session.add(user)
                session.commit()
                session.refresh(user)
            else:
                user = prev_user

        access_token = create_token(
            data=user.model_dump(),
            secret=ACCESS_SECRET_KEY,
            algorithm=ALGORITHM,
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        refresh_token = create_token(
            data=user.model_dump(),
            secret=REFRESH_SECRET_KEY,
            algorithm=ALGORITHM,
            expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
    except ValueError:
        raise HTTPException(401, "Invalid token")


@router.post("/refresh")
def refresh(body: Refresh):
    payload = get_payload_from_token(
        token=body.refresh_token,
        secret=REFRESH_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    user = get_user_by_id(payload["id"])

    if user is None:
        raise HTTPException(401, "Invalid token")

    access_token = create_token(
        data=user,
        secret=ACCESS_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = create_token(
        data=user,
        secret=REFRESH_SECRET_KEY,
        algorithm=ALGORITHM,
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
