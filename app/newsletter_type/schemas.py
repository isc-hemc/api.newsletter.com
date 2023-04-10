"""Newsletter Type schemas module."""
from utils import ma

from .models import NewsletterType


class NewsletterTypeSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `NewsletterType` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = NewsletterType
        dump_only = ("id", "created_at", "updated_at")


__all__ = ["NewsletterTypeSchema"]
