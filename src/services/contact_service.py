from sqlmodel import Session

from models.contact_model import Contact


def create(contact: Contact, session: Session):
    session.add(contact)
    session.commit()
    session.refresh(contact)

    return contact
