from pydantic import BaseModel

from models.avatar_model import Avatar


class AvatarReq(BaseModel):
    link: str

    name: str | None = None
    details: str | None = None

    def pre_insert(self, *, user_id: int):
        return Avatar(**self.model_dump(), user_id=user_id)


class AvatarRes(AvatarReq):
    id: int
    user_id: int
