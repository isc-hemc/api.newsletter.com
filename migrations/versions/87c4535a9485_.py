"""empty message

Revision ID: 87c4535a9485
Revises: c8aaf0ab9eec
Create Date: 2023-04-04 03:02:05.955753

"""
import datetime
import uuid

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "87c4535a9485"
down_revision = "c8aaf0ab9eec"
branch_labels = None
depends_on = None

SUBSCRIPTIONS = [
    {
        "id": uuid.uuid4(),
        "name": "Beneficios",
        "description": None,
        "tag": "benefits",
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "id": uuid.uuid4(),
        "name": "Novedades",
        "description": None,
        "tag": "news",
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "id": uuid.uuid4(),
        "name": "Promociones",
        "description": None,
        "tag": "promotions",
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "id": uuid.uuid4(),
        "name": "Recompensas",
        "description": None,
        "tag": "rewards",
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    subscriptions = op.create_table(
        "subscriptions",
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("tag", sa.String(length=64), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("tag"),
    )
    op.bulk_insert(subscriptions, SUBSCRIPTIONS)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscriptions")
    # ### end Alembic commands ###