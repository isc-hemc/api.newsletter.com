"""Contact models module."""
import uuid
from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from utils import db


class ContactModel(db.Model):
    """Extend from `db.Model` and define the fields for a Contact registry.

    Attributes
    ----------
    id : sa.Column
        Registry unique identifier.
    name : sa.Column
        Contact name, this field is required.
    last_name : sa.Column
        Contact last name, this field is required.
    email : sa.Column
        Contact email, this field is unique and required.
    is_active : sa.Column
        True if the registry is active, otherwise False.
    created_at : sa.Column
        Date when the registry was created.
    updated_at : sa.Column
        Date when the registry was updated.

    """

    __tablename__ = "contacts"

    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = sa.Column(sa.String(32), nullable=False)
    last_name = sa.Column(sa.String(32), nullable=False)
    email = sa.Column(sa.String(120), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime(timezone=True), default=func.now())
    updated_at = sa.Column(
        sa.DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    @classmethod
    def find_all(self) -> List["ContactModel"]:
        """Query all resources."""
        return self.query.all()

    @classmethod
    def find_by_email(self, _email: str) -> Optional["ContactModel"]:
        """Query a single user by the given email."""
        return self.query.filter_by(email=_email).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["ContactModel"]
