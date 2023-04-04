"""Newsletter schemas module."""
from utils import ma

from .models import Newsletter


class NewsletterSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `Newsletter` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = Newsletter
        dump_only = ("id", "created_at", "updated_at")
        include_fk = True


__all__ = ["NewsletterSchema"]
