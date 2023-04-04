"""Subscription models module."""
import sqlalchemy as sa

from utils import BaseModel, db


class Subscription(db.Model, BaseModel):
    """Declaration of the Subscription model.

    Attributes
    ----------
    name : sa.Column
        Subscription name, this field is required and unique.
    description : sa.Column
        Subscription description, this field is optional.

    """

    __tablename__ = "subscriptions"

    name = sa.Column(sa.String(128), nullable=False, unique=True)
    description = sa.Column(sa.Text, default=None, nullable=True)


__all__ = ["Subscription"]
