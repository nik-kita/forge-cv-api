from pydantic import BaseModel

from models.language_model import Language


class LanguageReq(BaseModel):
    language: str

    level: str | None = None
    certificate: str | None = None
    details: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Language(**self.model_dump(), user_id=user_id, profile_id=profile_id)


class LanguageRes(LanguageReq):
    id: int
    user_id: int
    profile_id: int | None = None
