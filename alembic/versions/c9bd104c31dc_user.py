"""user

Revision ID: c9bd104c31dc
Revises: 56768cdb72cc
Create Date: 2024-04-02 00:53:46.892375

"""
from database.models.versions.user_c9bd104c31dc import Userc9bd104c31dc
from database.db import engine
from sqlmodel import SQLModel
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9bd104c31dc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class User(Userc9bd104c31dc, table=True):
    __tablename__ = 'users'


def upgrade() -> None:
    User.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(User.__tablename__)
