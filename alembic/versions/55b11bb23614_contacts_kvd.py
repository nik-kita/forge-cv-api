"""contacts_kvd

Revision ID: 55b11bb23614
Revises: 3157dda778eb
Create Date: 2024-04-02 03:34:45.720243

"""
from src.database.db import engine
from src.database.models.versions.contacts_kvd_55b11bb23614 import ContactsKvd_55b11bb23614
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55b11bb23614'
down_revision: Union[str, None] = '3157dda778eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class ContactsKvd(ContactsKvd_55b11bb23614, table=True):
    __tablename__ = "contacts_kvd"

def upgrade() -> None:
    ContactsKvd.metadata.create_all(engine)


def downgrade() -> None:
    op.drop_table(ContactsKvd.__tablename__)
