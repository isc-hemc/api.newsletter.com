"""Newsletter urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import NewsletterResource

NEWSLETTER_BLUEPRINT = Blueprint("NEWSLETTER_BLUEPRINT", __name__)

api = Api(NEWSLETTER_BLUEPRINT)
api.add_resource(NewsletterResource, "/v1/newsletter")

__all__ = ["NEWSLETTER_BLUEPRINT"]
