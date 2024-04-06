from sqlmodel import Relationship
from models.avatar_model import Avatar
from models.education_model import Education
from models.experience_model import Experience
from models.language_model import Language
from models.profiles_many_to_many import ProfilesContacts, ProfilesEducations, ProfilesExperiences, ProfilesLanguages, ProfilesSkills
from models.skill_model import Skill
from models.contact_model import Contact


from sqlmodel import SQLModel, Field


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    avatar_id: int | None = Field(foreign_key='avatars.id')
    name: str | None = Field(default='default')
    summary: str | None
    details: str | None

    contacts: list[Contact] = Relationship(link_model=ProfilesContacts)
    skills: list[Skill] = Relationship(link_model=ProfilesSkills)
    education: list[Education] = Relationship(link_model=ProfilesEducations)
    experience: list[Experience] = Relationship(link_model=ProfilesExperiences)
    languages: list[Language] = Relationship(link_model=ProfilesLanguages)

    avatar: Avatar = Relationship()
