"""Contacts schemas module."""
from utils import ma

from .models import ContactModel


class ContactSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `ContactModel` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = ContactModel
        dump_only = ("id", "created_at", "updated_at")


__all__ = ["ContactSchema"]
