"""Newsletter Type resources module."""
from utils import ListResource

from .models import NewsletterType
from .schemas import NewsletterTypeSchema


class NewsletterTypeListResource(ListResource):
    """Extends from `ListResource` and manage a list of newsletter-types."""

    model = NewsletterType
    schema_class = NewsletterTypeSchema


__all__ = ["NewsletterTypeListResource"]
