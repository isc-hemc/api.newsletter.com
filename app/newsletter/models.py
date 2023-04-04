"""Newsletter models module."""
from sqlalchemy import Column, String

from utils import BaseModel, db


class Newsletter(db.Model, BaseModel):
    """Declaration of the Newsletter model.

    Attributes
    ----------
    subject : Column
        Newsletter subject message, this field is required.

    """

    __tablename__ = "newsletters"

    subject = Column(String(256), nullable=False)

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["Newsletter"]
