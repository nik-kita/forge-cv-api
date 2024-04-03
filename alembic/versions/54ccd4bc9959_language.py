"""language

Revision ID: 54ccd4bc9959
Revises: 664929d99358
Create Date: 2024-04-02 09:47:13.192530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from database.models.versions.language_54ccd4bc9959 import Language_54ccd4bc9959
from database.db import engine

# revision identifiers, used by Alembic.
revision: str = '54ccd4bc9959'
down_revision: Union[str, None] = '664929d99358'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Language(Language_54ccd4bc9959, table=True):
    __tablename__ = "languages"


def upgrade() -> None:
    Language.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(Language.__tablename__)
