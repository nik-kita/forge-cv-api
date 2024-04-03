"""alter user with auth_provider

Revision ID: ed2df492986b
Revises: 4451bbbfbdbd
Create Date: 2024-04-02 01:45:32.162475

"""
from src.database.models.versions.auth_provider_4451bbbfbdbd import AuthProvider4451bbbfbdbd
from src.database.models.versions.user_ed2df492986b import Userced2df492986b
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum


# revision identifiers, used by Alembic.
revision: str = 'ed2df492986b'
down_revision: Union[str, None] = '4451bbbfbdbd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(Userced2df492986b.__tablename__, sa.Column(
        'auth', Enum(AuthProvider4451bbbfbdbd), nullable=False))


def downgrade() -> None:
    op.drop_column(Userced2df492986b.__tablename__, 'auth')
