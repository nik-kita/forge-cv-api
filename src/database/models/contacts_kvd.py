from sqlmodel import Session
from .versions.contacts_kvd_55b11bb23614 import ContactsKvd_55b11bb23614


BaseContactsKvd = ContactsKvd_55b11bb23614


class ContactsKvd(BaseContactsKvd, table=True):
    __tablename__ = "contacts_kvd"


class ContactsKvdRes(BaseContactsKvd):
    pass


def create_contact(contact: ContactsKvd, session: Session):
    session.add(contact)
    session.commit()
    session.refresh(contact)

    return contact
