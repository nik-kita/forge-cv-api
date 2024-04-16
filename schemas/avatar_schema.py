from pydantic import BaseModel
from sqlmodel import Session, select

from models.avatar_model import Avatar


class AvatarReq(BaseModel):
    link: str

    name: str | None = None
    details: str | None = None

    def pre_insert(self, *, user_id: int):
        return Avatar(**self.model_dump(), user_id=user_id)

    def pre_upsert(self, *, user_id: int, session: Session):
        prev_sql = select(Avatar).where(
            Avatar.link == self.link,
            Avatar.name == self.name,
            Avatar.details == self.details,
            Avatar.user_id == user_id,
        )
        prev = session.exec(prev_sql).first()

        return prev or self.pre_insert(user_id=user_id)


class AvatarRes(AvatarReq):
    id: int
    user_id: int
