from pydantic import BaseModel
from sqlmodel import Session, select

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

    def pre_upsert(self, *, user_id: int, profile_id: int, session: Session):
        prev_check_sql = select(Experience).where(
            Experience.company == self.company,
            Experience.from_date == self.from_date,
            Experience.to_date == self.to_date,
            Experience.duration == self.duration,
            Experience.details == self.details,
            Experience.position == self.position,
            Experience.certificate == self.certificate,
            Experience.reference_letter == self.reference_letter,
            Experience.user_id == user_id,
        )
        prev = session.exec(prev_check_sql).first()

        return prev or self.pre_insert(user_id=user_id, profile_id=profile_id)


class ExperienceRes(ExperienceReq):
    id: int
    user_id: int
    profile_id: int | None = None
