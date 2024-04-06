from sqlmodel import SQLModel, Field


class _ProfileSide(SQLModel):
    profile_id: int | None = Field(
        foreign_key='profiles.id', primary_key=True,  default=None
    )


class ProfilesContacts(_ProfileSide, table=True):
    __tablename__ = 'profiles_contacts'

    contact_id: int | None = Field(
        foreign_key='contacts.id', primary_key=True,  default=None
    )


class ProfilesEducations(_ProfileSide, table=True):
    __tablename__ = 'profiles_educations'

    contact_id: int | None = Field(
        foreign_key='educations.id', primary_key=True,  default=None
    )


class ProfilesExperiences(_ProfileSide, table=True):
    __tablename__ = 'profiles_experiences'

    experience_id: int | None = Field(
        foreign_key='experiences.id', primary_key=True,  default=None
    )


class ProfilesLanguages(_ProfileSide, table=True):
    __tablename__ = 'profiles_languages'

    language_id: int | None = Field(
        foreign_key='languages.id', primary_key=True,  default=None
    )


class ProfilesSkills(_ProfileSide, table=True):
    __tablename__ = 'profiles_skills'

    skill_id: int | None = Field(
        foreign_key='skills.id', primary_key=True, default=None
    )
