"""Attachment models module."""
from sqlalchemy import Column, LargeBinary, String

from app.newsletter import Newsletter
from utils import BaseModel, db


class Attachment(db.Model, BaseModel):
    """Declaration of the Attachment model.

    Attributes
    ----------
    name : Column
        Attachment name, this field is required.
    mimetype : Column
        Attachment mimetype, this field es required.
    file : Column
        Binary representation of a PDF or PNG file, this field is required.

    """

    __tablename__ = "attachments"

    name = Column(String(128), nullable=False)
    mimetype = Column(String(32), nullable=False)
    file = Column(LargeBinary, nullable=False)

    newsletters = db.relationship(
        "Newsletter", backref="attachment", lazy=True
    )


__all__ = ["Attachment"]
