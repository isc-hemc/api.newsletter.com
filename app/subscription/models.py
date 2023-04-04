"""Subscription models module."""
from sqlalchemy import Column, String, Text

from utils import BaseModel, db


class Subscription(db.Model, BaseModel):
    """Declaration of the Subscription model.

    Attributes
    ----------
    name : Column
        Subscription name, this field is required and unique.
    description : Column
        Subscription description, this field is optional.

    """

    __tablename__ = "subscriptions"

    name = Column(String(128), nullable=False, unique=True)
    description = Column(Text, default=None, nullable=True)


__all__ = ["Subscription"]
