from pydantic import BaseModel

from models.auth_provider_enum import AuthProviderEnum


class SignIn(BaseModel):
    credential: str
    auth_provider: AuthProviderEnum


class Refresh(BaseModel):
    refresh_token: str


class RefreshRes(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    nik: None | str = None

class SignInRes(RefreshRes):
    pass
