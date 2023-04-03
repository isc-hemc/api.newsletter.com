"""Contact urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import ContactListResource, ContactResource

CONTACT_BLUEPRINT = Blueprint("CONTACT_BLUEPRINT", __name__)

api = Api(CONTACT_BLUEPRINT)
api.add_resource(ContactResource, "/v1/contacts")
api.add_resource(ContactListResource, "/v1/contacts")

__all__ = ["CONTACT_BLUEPRINT"]
