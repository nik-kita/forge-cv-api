from pydantic import BaseModel
from sqlmodel import Session, select

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

    def pre_upsert(self, *, user_id: int, profile_id: int, session: Session):
        prev_check_sql = select(Education).where(
            Education.university == self.university,
            Education.from_date == self.from_date,
            Education.to_date == self.to_date,
            Education.diploma == self.diploma,
            Education.certificate == self.certificate,
            Education.details == self.details,
            Education.education == self.education,
            Education.degree == self.degree,
            Education.user_id == user_id,
        )
        prev = session.exec(prev_check_sql).first()

        return prev or self.pre_insert(user_id=user_id, profile_id=profile_id)


class EducationRes(EducationReq):
    id: int
    user_id: int
    profile_id: int | None = None
