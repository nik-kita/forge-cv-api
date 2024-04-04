from pydantic import BaseModel


class SkillReq(BaseModel):
    user_id: int
    name: str
    level: int

    profile_id: int | None = None
    details: str | None = None
    certificate: str | None = None


class SkillRes(SkillReq):
    id: int
