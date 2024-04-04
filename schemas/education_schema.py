from pydantic import BaseModel


class EducationReq(BaseModel):
    user_id: int
    university: str

    profile_id: int | None = None
    from_date: str | None = None
    to_date: str | None = None
    diploma: str | None = None
    certificate: str | None = None
    details: str | None = None
    education: str | None = None
    degree: str | None = None


class EducationRes(EducationReq):
    id: int
