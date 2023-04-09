"""empty message

Revision ID: 0add3ee8fd8f
Revises: f6e2ae2cd686
Create Date: 2023-04-09 15:25:08.761110

"""
import datetime
import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0add3ee8fd8f"
down_revision = "f6e2ae2cd686"
branch_labels = None
depends_on = None


NEWSLETTER_TYPES = [
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
    newsletter_type = op.create_table(
        "newsletter_type",
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("tag", sa.String(length=64), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("tag"),
    )
    op.bulk_insert(newsletter_type, NEWSLETTER_TYPES)
    op.drop_table("subscriptions")
    with op.batch_alter_table("newsletters", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("newsletter_type_id", sa.UUID(), nullable=False)
        )
        batch_op.create_foreign_key(
            None, "newsletter_type", ["newsletter_type_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("newsletters", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("newsletter_type_id")

    op.create_table(
        "subscriptions",
        sa.Column(
            "name", sa.VARCHAR(length=64), autoincrement=False, nullable=False
        ),
        sa.Column(
            "description", sa.TEXT(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "tag", sa.VARCHAR(length=64), autoincrement=False, nullable=False
        ),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="subscriptions_pkey"),
        sa.UniqueConstraint("tag", name="subscriptions_tag_key"),
    )
    op.drop_table("newsletter_type")
    # ### end Alembic commands ###
