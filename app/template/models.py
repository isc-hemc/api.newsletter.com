"""Template models module."""
from typing import List, Optional

from sqlalchemy import Column, String, Text

from utils import BaseModel, db


class Template(db.Model, BaseModel):
    """Declaration of the Template model.

    Attributes
    ----------
    name : Column
        Template name, this field is required and unique.
    content : Column
        Template content, it can be HTML code, default is an empty-string.
    newsletters : relationship
        Association between template and newsletter.

    """

    __tablename__ = "templates"

    name = Column(String(128), nullable=False, unique=True)
    content = Column(Text, default="", nullable=True)

    newsletters = db.relationship("Newsletter", backref="template", lazy=True)

    @classmethod
    def find_all(self) -> List["Template"]:
        """Query all resources."""
        return self.query.all()

    @classmethod
    def find_by_id(self, _id: str) -> Optional["Template"]:
        """Query a single resource by the given id."""
        return self.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(self, _name: str) -> Optional["Template"]:
        """Query a single resource by the given name."""
        return self.query.filter_by(name=_name).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["Template"]
