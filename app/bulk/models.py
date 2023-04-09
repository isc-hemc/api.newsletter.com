"""Bulk models module."""
from typing import List, Optional

from sqlalchemy import Column, Integer, String

from app.contact import Contact
from utils import BaseModel, db


class Bulk(db.Model, BaseModel):
    """Declaration of the bulk model.

    Attributes
    ----------
    name : Column
        Custom name for the bulk, this field is required and unique.
    inserted : Column
        Number of inserted rows, defualt is `0`.
    errors : Column
        Number of errors detected in data, e.g. repeated data, defualt is `0`.

    """

    __tablename__ = "bulks"

    name = Column(String(64), nullable=False, unique=True)
    inserted = Column(Integer, default=0)
    errors = Column(Integer, default=0)

    contacts = db.relationship("Contact", backref="bulk", lazy=True)

    @classmethod
    def find_all(self) -> List["Bulk"]:
        """Query all resources."""
        return self.query.all()

    @classmethod
    def find_by_name(self, _name: str) -> Optional["Bulk"]:
        """Query a single resource by the given name."""
        return self.query.filter_by(name=_name).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update the current resource."""
        db.session.commit()


__all__ = ["Bulk"]
