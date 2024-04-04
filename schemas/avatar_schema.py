from pydantic import BaseModel


class AddAvatarReq(BaseModel):
    user_id: int
    link: str
    name: str | None = None
    details: str | None = None

class AvatarRes(BaseModel):
    id: int
    user_id: int
    link: str
    name: str | None = None
    details: str | None = None