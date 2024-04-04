from pydantic import BaseModel


class AvatarReq(BaseModel):
    user_id: int
    link: str

    name: str | None = None
    details: str | None = None


class AvatarRes(AvatarReq):
    id: int
