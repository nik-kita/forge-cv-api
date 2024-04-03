"""profile

Revision ID: 3157dda778eb
Revises: f11abea855d3
Create Date: 2024-04-02 02:37:00.298772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from database.models.versions.profile_3157dda778eb import Profile_3157dda778eb
from database.core import _engine
from sqlmodel import UniqueConstraint

# revision identifiers, used by Alembic.
revision: str = '3157dda778eb'
down_revision: Union[str, None] = 'f11abea855d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Profile(Profile_3157dda778eb, table=True):
    __tablename__ = "profiles"


UniqueConstraint(Profile.user_id, Profile.name)


def upgrade() -> None:
    Profile.metadata.create_all(_engine)


def downgrade() -> None:
    op.drop_table(Profile.__tablename__)
