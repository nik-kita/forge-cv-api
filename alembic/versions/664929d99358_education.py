"""education

Revision ID: 664929d99358
Revises: d41cd8f56f34
Create Date: 2024-04-02 09:31:15.816121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.database.models.versions.education_664929d99358 import Education_664929d99358
from src.database.db import engine

# revision identifiers, used by Alembic.
revision: str = '664929d99358'
down_revision: Union[str, None] = 'd41cd8f56f34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Education(Education_664929d99358, table=True):
    __tablename__ = "educations"


def upgrade() -> None:
    Education.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(Education.__tablename__)
