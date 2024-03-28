from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBearer
from typing import Annotated
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests
from .config import GOOGLE_CLIENT_ID, SWAGGER_HELPER_URL, SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

app = FastAPI()

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


@app.post("/sign-in")
def sign_in(sign_in: SignIn):
    try:
        print(sign_in)
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(
            sign_in.credential, requests.Request(), GOOGLE_CLIENT_ID
        )
        userid = idinfo["sub"]
    except ValueError:
        raise HTTPException(401, "Invalid token")

    return idinfo


@app.get("/me")
def get_me(token: Annotated[str, Depends(oauth2_schema)]):
    return token


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
