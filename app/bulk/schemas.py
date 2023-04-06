"""Bulk schemas module."""
from utils import ma

from .models import Bulk


class BulkSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `Bulk` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = Bulk
        dump_only = ("id", "created_at", "updated_at")


__all__ = ["BulkSchema"]
