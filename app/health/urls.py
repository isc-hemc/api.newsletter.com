"""Health urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import HealthResource

HEALTH_BLUEPRINT = Blueprint("HEALTH_BLUEPRINT", __name__)

api = Api(HEALTH_BLUEPRINT)
api.add_resource(HealthResource, "/v1/health")

__all__ = ["HEALTH_BLUEPRINT"]
