from pydantic import BaseModel
from typing import TypeVar, Generic
from schemas.avatar_schema import AvatarReq, AvatarRes
from schemas.contact_schema import ContactReq, ContactRes
from schemas.education_schema import EducationReq, EducationRes
from schemas.experience_schema import ExperienceReq, ExperienceRes
from schemas.language_schema import LanguageReq, LanguageRes
from schemas.skill_schema import SkillReq, SkillRes

T = TypeVar('T')

class ModifyProfileReq(BaseModel):
    name: str | None = None

    summary: str | None = None
    details: str | None = None
    contacts: list[ContactReq] | None = None
    skills: list[SkillReq] | None = None
    education: list[EducationReq] | None = None
    experience: list[ExperienceReq] | None = None
    languages: list[LanguageReq] | None = None
    avatar: AvatarReq | None = None


class ProfileReq(ModifyProfileReq):
    name: str


class ProfileRes(BaseModel):
    id: int
    user_id: int
    name: str

    summary: str | None = None
    details: str | None = None
    contacts: list[ContactRes] = []
    skills: list[SkillRes] = []
    education: list[EducationRes] = []
    experience: list[ExperienceRes] = []
    avatar: AvatarRes | None = None
    languages: list[LanguageRes] = []

class PaginatedRes(BaseModel, Generic[T]):
    items: list[T]
    total: int
    offset: int
    
