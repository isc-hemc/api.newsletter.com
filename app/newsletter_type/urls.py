"""Newsletter Type urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import NewsletterTypeListResource

NEWSLETTER_TYPE_BLUEPRINT = Blueprint("NEWSLETTER_TYPE_BLUEPRINT", __name__)

api = Api(NEWSLETTER_TYPE_BLUEPRINT)
api.add_resource(NewsletterTypeListResource, "/v1/newsletter-types")

__all__ = ["NEWSLETTER_TYPE_BLUEPRINT"]
