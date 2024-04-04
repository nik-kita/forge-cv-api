from sqlmodel import Session
from sqlmodel import SQLModel, Field


class BaseContactsKvd(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    profile_id: int | None = Field(foreign_key='profiles.id')
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    details: str | None = None


class ContactsKvd(BaseContactsKvd, table=True):
    __tablename__ = "contacts_kvd"


class ContactsKvdRes(BaseContactsKvd):
    pass


def create_contact(contact: ContactsKvd, session: Session):
    session.add(contact)
    session.commit()
    session.refresh(contact)

    return contact
