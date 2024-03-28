from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.security import (
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    OAuth2,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from fastapi.openapi.docs import get_swagger_ui_oauth2_redirect_html
from typing import Annotated
from fastapi.responses import HTMLResponse

from google.oauth2 import id_token
from google.auth.transport import requests


GOOGLE_CLIENT_ID = (
    "456894138702-b1hkcu9caadps4nv7bih3sr4v2c3tmtg.apps.googleusercontent.com"
)
GOOGLE_REDIRECT_URI = "http://localhost:3000/token"

app = FastAPI()

oauth2_schema = HTTPBearer(
    description=f"""
# [Sign in with Google](https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline)
""",
)




@app.post("/sign-in")
def token(req: Request):
    try:
        print(req.query_params)
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(req.query_params, requests.Request(), GOOGLE_CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo["sub"]
    except ValueError:
        # Invalid token
        pass

    return "hi"
