"""Contact urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import (
    ContactListResource,
    ContactResource,
    ContactSubscriptionListResource,
    ContactSubscriptionResource,
)

CONTACT_BLUEPRINT = Blueprint("CONTACT_BLUEPRINT", __name__)

api = Api(CONTACT_BLUEPRINT)
api.add_resource(ContactResource, "/v1/contacts")
api.add_resource(ContactListResource, "/v1/contacts")
api.add_resource(
    ContactSubscriptionResource,
    "/v1/contacts/<string:contact_id>/subscriptions/<string:subscription_id>",
)
api.add_resource(
    ContactSubscriptionListResource,
    "/v1/contacts/<string:contact_id>/subscriptions",
)

__all__ = ["CONTACT_BLUEPRINT"]
