"""Newsletter Type models module."""
from typing import List

from sqlalchemy import Column, String, Text

from utils import BaseModel, db


class NewsletterType(db.Model, BaseModel):
    """Declaration of the Newsletter Type model.

    Attributes
    ----------
    name : Column
        Newsletter Type name, this field is required.
    description : Column
        Newsletter Type description, this field is optional.
    tag : Column
        Newsletter Type identifier, this field is required and unique.

    """

    __tablename__ = "newsletter_type"

    name = Column(String(64), nullable=False)
    description = Column(Text, default=None, nullable=True)
    tag = Column(String(64), nullable=False, unique=True)

    newsletters = db.relationship(
        "Newsletter", backref="newsletter_type", lazy=True
    )

    @classmethod
    def find_all(self) -> List["NewsletterType"]:
        """Query all resources."""
        return self.query.all()


__all__ = ["NewsletterType"]
