"""Contacts urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import ContactListResource, ContactResource

CONTACTS_BLUEPRINT = Blueprint("CONTACTS_BLUEPRINT", __name__)

api = Api(CONTACTS_BLUEPRINT)
api.add_resource(ContactResource, "/v1/contacts")
api.add_resource(ContactListResource, "/v1/contacts")

__all__ = ["CONTACTS_BLUEPRINT"]
