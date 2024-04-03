from sqlmodel import Relationship
from src.database.models.avatar import Avatar
from src.database.models.education import Education
from src.database.models.experience import Experience
from src.database.models.language import Language
from src.database.models.skill import Skill
from .versions.profile_3157dda778eb import Profile_3157dda778eb
from .contacts_kvd import ContactsKvd


BaseProfile = Profile_3157dda778eb


class Profile(BaseProfile, table=True):
    __tablename__ = "profiles"

    contacts: list[ContactsKvd] = Relationship()
    skills: list[Skill] = Relationship()
    education: list[Education] = Relationship()
    experience: list[Experience] = Relationship()
    avatar: Avatar = Relationship()
    languages: list[Language] = Relationship()


class ProfileRes(BaseProfile):
    contacts: list[ContactsKvd] = []
    skills: list[Skill] = []
    education: list[Education] = []
    experience: list[Experience] = []
    avatar: Avatar | None = None
    languages: list[Language] = []