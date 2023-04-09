"""Contact models module."""
from typing import List, Optional

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from utils import BaseModel, db


class Contact(db.Model, BaseModel):
    """Declaration of the Contact model.

    Attributes
    ----------
    name : Column
        Contact name, this field is required.
    last_name : Column
        Contact last name, this field is required.
    email : Column
        Contact email, this field is unique and required.
    bulk_id : Column
        Foreign key of a bulk registry, this field is optional.

    """

    __tablename__ = "contacts"

    name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String(120), nullable=False, unique=True)

    bulk_id = Column(UUID(as_uuid=True), ForeignKey("bulks.id"), nullable=True)

    @classmethod
    def find_all(self) -> List["Contact"]:
        """Query all resources."""
        return self.query.all()

    @classmethod
    def find_by_bulk_id(self, _id: str) -> Optional["Contact"]:
        """Query a single resource by the given bulk ID."""
        return self.query.filter_by(bulk_id=_id)

    @classmethod
    def find_by_email(self, _email: str) -> Optional["Contact"]:
        """Query a single resource by the given email."""
        return self.query.filter_by(email=_email).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["Contact"]
