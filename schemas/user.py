from pydantic import BaseModel

from schemas.profile import ProfileRes


class UserRes(BaseModel):
    profiles: list[ProfileRes] = []
