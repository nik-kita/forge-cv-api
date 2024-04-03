from .versions.experience_d41cd8f56f34 import Experience_d41cd8f56f34


BaseExperience = Experience_d41cd8f56f34


class Experience(BaseExperience, table=True):
    __tablename__ = "experiences"
