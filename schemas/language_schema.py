from pydantic import BaseModel


class LanguageReq(BaseModel):
    user_id: int
    language: str

    profile_id: int | None = None
    level: str | None = None
    certificate: str | None = None
    details: str | None = None


class LanguageRes(LanguageReq):
    id: int
