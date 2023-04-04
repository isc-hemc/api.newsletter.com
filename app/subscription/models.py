"""Subscription models module."""
from sqlalchemy import Column, String, Text

from utils import BaseModel, db


class Subscription(db.Model, BaseModel):
    """Declaration of the Subscription model.

    Attributes
    ----------
    name : Column
        Subscription name, this field is required.
    description : Column
        Subscription description, this field is optional.
    tag : Column
        Subscription identifier, this field is required and unique.

    """

    __tablename__ = "subscriptions"

    name = Column(String(64), nullable=False)
    description = Column(Text, default=None, nullable=True)
    tag = Column(String(64), nullable=False, unique=True)


__all__ = ["Subscription"]
