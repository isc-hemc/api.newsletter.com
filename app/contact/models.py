"""Contact models module."""
from typing import List, Optional

import sqlalchemy as sa

from utils import BaseModel, db


class Contact(db.Model, BaseModel):
    """Declaration of the Contact model.

    Attributes
    ----------
    name : sa.Column
        Contact name, this field is required.
    last_name : sa.Column
        Contact last name, this field is required.
    email : sa.Column
        Contact email, this field is unique and required.

    """

    __tablename__ = "contacts"

    name = sa.Column(sa.String(32), nullable=False)
    last_name = sa.Column(sa.String(32), nullable=False)
    email = sa.Column(sa.String(120), nullable=False, unique=True)

    @classmethod
    def find_all(self) -> List["Contact"]:
        """Query all resources."""
        return self.query.all()

    @classmethod
    def find_by_email(self, _email: str) -> Optional["Contact"]:
        """Query a single user by the given email."""
        return self.query.filter_by(email=_email).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["Contact"]
