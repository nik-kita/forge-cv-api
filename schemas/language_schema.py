from pydantic import BaseModel
from sqlmodel import Session, select

from models.language_model import Language


class LanguageReq(BaseModel):
    language: str

    level: str | None = None
    certificate: str | None = None
    details: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Language(**self.model_dump(), user_id=user_id, profile_id=profile_id)

    def pre_upsert(self, *, user_id: int, profile_id: int, session: Session):
        prev_check_sql = select(Language).where(
            Language.user_id == user_id,
            Language.level == self.level,
            Language.certificate == self.certificate,
            Language.details == self.details,
        )
        prev = session.exec(prev_check_sql).first()

        return prev or self.pre_insert(user_id=user_id, profile_id=profile_id)


class LanguageRes(LanguageReq):
    id: int
    user_id: int
    profile_id: int | None = None
