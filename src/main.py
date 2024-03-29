from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests
from .config import (
    GOOGLE_CLIENT_ID,
    SWAGGER_HELPER_URL,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from sqlmodel import create_engine, SQLModel, Field, Session, select


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
            user = session.exec(select(User).where(User.email == user.email)).first()

            if user.id is None:
                session.add(user)
                session.commit()
                session.refresh(user)

        access_token = create_access_token(
            data=user.model_dump(),
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )

        return {"access_token": access_token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(401, "Invalid token")


@app.get("/me")
async def get_me(
    auth_credentials: Annotated[HTTPAuthorizationCredentials, Depends(oauth2_schema)]
):
    id = get_id_from_token(auth_credentials.credentials)
    me = get_user_by_id(id)
    return me


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    print(to_encode)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_id_from_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    id: str | None = None

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return id


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
