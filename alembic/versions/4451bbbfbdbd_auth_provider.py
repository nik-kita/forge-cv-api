"""auth-provider

Revision ID: 4451bbbfbdbd
Revises: c9bd104c31dc
Create Date: 2024-04-02 01:25:27.521319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from database.db import engine
from database.models.versions.auth_provider_4451bbbfbdbd import AuthProvider4451bbbfbdbd
from sqlmodel import SQLModel, Enum

# revision identifiers, used by Alembic.
revision: str = '4451bbbfbdbd'
down_revision: Union[str, None] = 'c9bd104c31dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    Enum(AuthProvider4451bbbfbdbd, name=AuthProvider4451bbbfbdbd.__name__).create(engine)


def downgrade() -> None:
    sa.Enum(AuthProvider4451bbbfbdbd.__name__).drop(engine)
