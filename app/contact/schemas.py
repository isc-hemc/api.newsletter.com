"""Contact schemas module."""
from utils import ma

from .models import Contact


class ContactSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `Contact` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = Contact
        dump_only = ("id", "created_at", "updated_at")
        include_fk = True


__all__ = ["ContactSchema"]
