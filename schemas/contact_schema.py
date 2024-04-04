from pydantic import BaseModel


class ContactReq(BaseModel):
    user_id: int
    key: str
    value: str

    profile_id: int | None = None
    details: str | None = None


class ContactRes(ContactReq):
    id: int
