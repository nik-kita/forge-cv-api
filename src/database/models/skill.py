from .versions.skill_c5b2e6ef6c14 import Skill_c5b2e6ef6c14

BaseSkill = Skill_c5b2e6ef6c14


class Skill(BaseSkill, table=True):
    __tablename__ = "skills"
