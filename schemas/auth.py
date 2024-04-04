from pydantic import BaseModel

from models.auth_provider import AuthProviderEnum


class SignIn(BaseModel):
    credential: str
    auth_provider: AuthProviderEnum


class Refresh(BaseModel):
    refresh_token: str
