"""Bulk urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import BulkListResource, BulkResource

BULK_BLUEPRINT = Blueprint("BULK_BLUEPRINT", __name__)

api = Api(BULK_BLUEPRINT)
api.add_resource(BulkResource, "/v1/bulks")
api.add_resource(BulkListResource, "/v1/bulks")

__all__ = ["BULK_BLUEPRINT"]
