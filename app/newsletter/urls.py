"""Newsletter urls module."""
from flask import Blueprint
from flask_restful import Api

from .resources import NewsletterResource, NewsletterSubmissionResource

NEWSLETTER_BLUEPRINT = Blueprint("NEWSLETTER_BLUEPRINT", __name__)

api = Api(NEWSLETTER_BLUEPRINT)
api.add_resource(NewsletterResource, "/v1/newsletters")
api.add_resource(
    NewsletterSubmissionResource, "/v1/newsletters/<string:id>/submissions"
)

__all__ = ["NEWSLETTER_BLUEPRINT"]
