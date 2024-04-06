from pydantic import BaseModel
from sqlmodel import Session, select

from models.skill_model import Skill


class SkillReq(BaseModel):
    name: str

    details: str | None = None
    certificate: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Skill(**self.model_dump(), user_id=user_id, profile_id=profile_id)

    def pre_upsert(self, *, user_id: int, profile_id: int, session: Session):
        prev_check_sql = select(Skill).where(
            Skill.name == self.name,
            Skill.details == self.details,
            Skill.certificate == self.certificate,
            Skill.user_id == user_id

        )
        prev = session.exec(prev_check_sql).first()

        return prev or self.pre_insert(user_id=user_id, profile_id=profile_id)


class SkillRes(SkillReq):
    profile_id: int | None = None
    user_id: int
    id: int
