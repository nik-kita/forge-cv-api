"""skill

Revision ID: c5b2e6ef6c14
Revises: 55b11bb23614
Create Date: 2024-04-02 03:45:08.210918

"""
from database.db import engine
from database.models.versions.skill_c5b2e6ef6c14 import Skill_c5b2e6ef6c14
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5b2e6ef6c14'
down_revision: Union[str, None] = '55b11bb23614'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Skill(Skill_c5b2e6ef6c14, table=True):
    __tablename__ = "skills"


def upgrade() -> None:
    Skill.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(Skill.__tablename__)
