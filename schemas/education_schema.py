from pydantic import BaseModel

from models.education_model import Education


class EducationReq(BaseModel):
    university: str

    from_date: str | None = None
    to_date: str | None = None
    diploma: str | None = None
    certificate: str | None = None
    details: str | None = None
    education: str | None = None
    degree: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Education(**self.model_dump(), user_id=user_id, profile_id=profile_id)


class EducationRes(EducationReq):
    id: int
    user_id: int
    profile_id: int | None = None
