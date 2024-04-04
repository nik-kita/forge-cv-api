from pydantic import BaseModel

from models.avatar import Avatar
from models.contacts_kvd import ContactsKvd
from models.education import Education
from models.experience import Experience
from models.language import Language
from models.skill import Skill


class UpsertProfile(BaseModel):
    contacts: list[ContactsKvd] | None = None
    skills: list[Skill] | None = None
    education: list[Education] | None = None
    experience: list[Experience] | None = None
    languages: list[Language] | None = None
    avatar: Avatar | None = None
