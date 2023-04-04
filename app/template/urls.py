"""Template urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import TemplateListResource, TemplateResource

TEMPLATE_BLUEPRINT = Blueprint("TEMPLATE_BLUEPRINT", __name__)

api = Api(TEMPLATE_BLUEPRINT)
api.add_resource(TemplateResource, "/v1/templates")
api.add_resource(TemplateListResource, "/v1/templates")

__all__ = ["TEMPLATE_BLUEPRINT"]
