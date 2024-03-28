from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBearer
from typing import Annotated
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests
from .config import GOOGLE_CLIENT_ID, SWAGGER_HELPER_URL


app = FastAPI()

oauth2_schema = HTTPBearer(
    description=f"""
# [Sign in with Google]({SWAGGER_HELPER_URL})
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
