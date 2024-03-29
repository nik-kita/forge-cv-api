from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from typing import Annotated
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests
from .config import (
    GOOGLE_CLIENT_ID,
    SWAGGER_HELPER_URL,
    ACCESS_SECRET_KEY,
    REFRESH_SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
)
from datetime import timedelta
from sqlmodel import create_engine, SQLModel, Field, Session, select
from .utils.jwt import get_payload_from_token, create_token

app = FastAPI()

oauth2_schema = HTTPBearer(
    description=f"""
#### How to get access token
1. [Sign in with Google]({SWAGGER_HELPER_URL})
2. Token from step 1 should be used in `/sign-in` endpoint
3. Access token from `/sign-in` insert into input below
""",
)


class BaseUser(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class User(BaseUser, table=True):
    email: str | None = Field(str, unique=True)
    sub: str | None = Field(str, unique=True)


class SignIn(BaseModel):
    credential: str


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


@app.post("/sign-in")
def sign_in(sign_in: SignIn):
    try:
        idinfo = id_token.verify_oauth2_token(
            sign_in.credential, requests.Request(), GOOGLE_CLIENT_ID
        )
        idinfo["sub"]
        print(idinfo)

        user = User(sub=idinfo["sub"], email=idinfo["email"])

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


class Refresh(BaseModel):
    refresh_token: str


@app.post("/refresh")
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


@app.get("/me")
async def get_me(
    auth_credentials: Annotated[HTTPAuthorizationCredentials, Depends(oauth2_schema)]
):
    payload = get_payload_from_token(
        token=auth_credentials.credentials,
        secret=ACCESS_SECRET_KEY,
        algorithms=[ALGORITHM],
    )
    me = get_user_by_id(payload["id"])
    return me


def get_user_by_email(email: str):
    user = None
    with Session(engine) as session:
        sql_query = select(User).where(User.email == email)
        user = session.exec(sql_query).first().model_dump()

    return user


def get_user_by_id(id: int):
    user = None
    with Session(engine) as session:
        sql_query = select(User).where(User.id == id)
        user = session.exec(sql_query).first().model_dump()

    return user
