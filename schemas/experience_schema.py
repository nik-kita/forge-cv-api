from pydantic import BaseModel


class ExperienceReq(BaseModel):
    user_id: int
    company: str

    profile_id: int | None = None
    from_date: str | None = None
    to_date: str | None = None
    duration: str | None = None
    details: str | None = None
    position: str | None = None
    certificate: str | None = None
    reference_letter: str | None = None


class ExperienceRes(ExperienceReq):
    id: int
