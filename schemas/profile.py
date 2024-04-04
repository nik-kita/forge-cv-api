from pydantic import BaseModel

from models.avatar import Avatar
from models.contacts_kvd import ContactsKvd
from models.education import Education
from models.experience import Experience
from models.language import Language
from models.profile import BaseProfile, FullProfile
from models.skill import Skill


class UpsertProfile(BaseModel):
    name: str
    contacts: list[ContactsKvd] | None = None
    skills: list[Skill] | None = None
    education: list[Education] | None = None
    experience: list[Experience] | None = None
    languages: list[Language] | None = None
    avatar: Avatar | None = None


class UpsertProfileRes(FullProfile):
    contacts: list[ContactsKvd] = []
    skills: list[Skill] = []
    education: list[Education] = []
    experience: list[Experience] = []
    avatar: Avatar | None = None
    languages: list[Language] = []
