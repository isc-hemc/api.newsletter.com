"""Template schemas module."""
from utils import ma

from .models import Template


class TemplateSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `Template` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = Template
        dump_only = ("id", "created_at", "updated_at")


__all__ = ["TemplateSchema"]
