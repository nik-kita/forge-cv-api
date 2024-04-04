from pydantic import BaseModel

from models.experience_model import Experience


class ExperienceReq(BaseModel):
    company: str

    from_date: str | None = None
    to_date: str | None = None
    duration: str | None = None
    details: str | None = None
    position: str | None = None
    certificate: str | None = None
    reference_letter: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Experience(**self.model_dump(), user_id=user_id, profile_id=profile_id)


class ExperienceRes(ExperienceReq):
    id: int
    user_id: int
    profile_id: int | None = None
