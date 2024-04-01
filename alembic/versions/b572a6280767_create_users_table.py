"""create users table

Revision ID: b572a6280767
Revises: 
Create Date: 2024-03-30 01:27:32.425115

"""

from src.database.db import get_session
from src.database.models.versions.user_b572a6280767 import User
from typing import Sequence, Union
from sqlmodel import SQLModel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b572a6280767"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    SQLModel.metadata.create_all(get_session())    


def downgrade() -> None:
    op.drop_table(User.__tablename__)
