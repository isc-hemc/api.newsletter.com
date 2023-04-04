"""Template models module."""
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

    """

    __tablename__ = "templates"

    name = Column(String(128), nullable=False, unique=True)
    content = Column(Text, default="", nullable=True)


__all__ = ["Template"]
