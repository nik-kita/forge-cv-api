"""create users table

Revision ID: b572a6280767
Revises: 
Create Date: 2024-03-30 01:27:32.425115

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b572a6280767"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("email", sa.String, unique=True, nullable=True),
        sa.Column("sub", sa.String, unique=True, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("users")
