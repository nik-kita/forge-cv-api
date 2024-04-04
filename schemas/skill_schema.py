from pydantic import BaseModel

from models.skill_model import Skill


class SkillReq(BaseModel):
    name: str

    details: str | None = None
    certificate: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Skill(**self.model_dump(), user_id=user_id, profile_id=profile_id)


class SkillRes(SkillReq):
    profile_id: int | None = None
    user_id: int
    id: int
