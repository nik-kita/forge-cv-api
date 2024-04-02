"""experience

Revision ID: d41cd8f56f34
Revises: c5b2e6ef6c14
Create Date: 2024-04-02 09:13:44.774987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.database.models.versions.experience_d41cd8f56f34 import Experience_d41cd8f56f34
from src.database.db import engine

# revision identifiers, used by Alembic.
revision: str = 'd41cd8f56f34'
down_revision: Union[str, None] = 'c5b2e6ef6c14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Experience(Experience_d41cd8f56f34, table=True):
    __tablename__ = "experiences"


def upgrade() -> None:
    Experience.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(Experience.__tablename__)
