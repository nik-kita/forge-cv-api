from sqlmodel import Relationship
from models.avatar import Avatar
from models.education import Education
from models.experience import Experience
from models.language import Language
from models.skill import Skill
from .contacts_kvd import ContactsKvd


from sqlmodel import SQLModel, Field


class Profile(SQLModel, table=True):
    __tablename__ = "profiles"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id', nullable=False)
    avatar_id: int | None = Field(foreign_key='avatars.id')

    name: str | None = Field(default='default')
    summary: str | None
    details: str | None

    contacts: list[ContactsKvd] = Relationship()
    skills: list[Skill] = Relationship()
    education: list[Education] = Relationship()
    experience: list[Experience] = Relationship()
    avatar: Avatar = Relationship()
    languages: list[Language] = Relationship()
