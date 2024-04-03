"""avatar

Revision ID: f11abea855d3
Revises: ed2df492986b
Create Date: 2024-04-02 02:30:14.316685

"""
from database.db import engine
from database.models.versions.avatar_f11abea855d3 import Avatar_f11abea855d3
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f11abea855d3'
down_revision: Union[str, None] = 'ed2df492986b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Avatar(Avatar_f11abea855d3, table=True):
    __tablename__ = "avatars"


def upgrade() -> None:
    Avatar.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(Avatar.__tablename__)
