from pydantic import BaseModel

from schemas.profile_schema import ProfileRes


class UserRes(BaseModel):
    profiles: list[ProfileRes] = []


class PublicUserRes(BaseModel):
    nik: str | None
