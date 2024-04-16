from pydantic import BaseModel
from sqlmodel import Session, select

from models.contact_model import Contact


class ContactReq(BaseModel):
    key: str
    value: str

    details: str | None = None

    def pre_insert(self, *, user_id: int, profile_id: int | None = None):
        return Contact(**self.model_dump(), user_id=user_id, profile_id=profile_id)

    def pre_upsert(self, *, user_id: int, profile_id: int, session: Session):
        prev_check_sql = select(Contact).where(
            Contact.key == self.key,
            Contact.value == self.value,
            Contact.user_id == user_id,
        )

        prev = session.exec(prev_check_sql).first()

        return prev or self.pre_insert(user_id=user_id, profile_id=profile_id)


class ContactRes(ContactReq):
    id: int
    user_id: int
    profile_id: int | None = None
