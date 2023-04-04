"""Utility models module."""
import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class BaseModel:
    """Model base class with predefined attributes.

    Attributes
    ----------
    id : sa.Column
        Registry unique identifier.
    is_active : sa.Column
        True if the registry is active, otherwise False.
    created_at : sa.Column
        Date when the registry was created.
    updated_at : sa.Column
        Date when the registry was updated.

    """

    id = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime(timezone=True), default=func.now())
    updated_at = sa.Column(
        sa.DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


__all__ = ["BaseModel"]
