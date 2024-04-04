from sqlmodel import Relationship
from models.avatar_model import Avatar
from models.education_model import Education
from models.experience_model import Experience
from models.language_model import Language
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

    contacts: list[Contact] = Relationship()
    skills: list[Skill] = Relationship()
    education: list[Education] = Relationship()
    experience: list[Experience] = Relationship()
    avatar: Avatar = Relationship()
    languages: list[Language] = Relationship()
