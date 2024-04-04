from pydantic import BaseModel

from models.contact_model import Contact


class ContactReq(BaseModel):
    key: str
    value: str

    details: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Contact(**self.model_dump(), user_id=user_id, profile_id=profile_id)


class ContactRes(ContactReq):
    id: int
    user_id: int
    profile_id: int | None = None
