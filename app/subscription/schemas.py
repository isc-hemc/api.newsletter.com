"""Subscription schemas module."""
from utils import ma

from .models import Subscription


class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    """Transform a queryset of `Subscription` into a native Python datatype."""

    class Meta:
        """Inner Meta class."""

        model = Subscription
        dump_only = ("id", "created_at", "updated_at")
        include_fk = True


__all__ = ["SubscriptionSchema"]
