from fastapi import Depends, FastAPI
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials
from src.config import ACCESS_SECRET_KEY, ALGORITHM
from src.database.user import get_user_by_id
from .utils.jwt import get_payload_from_token
from .routers.auth import router as auth_router, oauth2_schema

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])


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
