"""Utility models module."""
import uuid

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class BaseModel:
    """Model base class with predefined attributes.

    Attributes
    ----------
    id : Column
        Registry unique identifier.
    created_at : Column
        Date when the registry was created.
    updated_at : Column
        Date when the registry was updated.

    """

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


__all__ = ["BaseModel"]
