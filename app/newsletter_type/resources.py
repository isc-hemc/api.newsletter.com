"""Newsletter Type resources module."""
from flask_restful import Resource

from .models import NewsletterType
from .schemas import NewsletterTypeSchema


class NewsletterTypeListResource(Resource):
    """Manage a list of newsletter-types.

    Attributes
    ----------
    schema : NewsletterTypeSchema
        Serialization schema object.

    Methods
    -------
    get()
        Retrieve a list of serialized newsletter-types.

    """

    schema = NewsletterTypeSchema(many=True)

    def get(self):
        """Retrieve a list of serialized newsletter-types."""
        newsletter_types = NewsletterType.find_all()

        serialized_data = self.schema.dump(newsletter_types)

        return {"results": serialized_data}, 200


__all__ = ["NewsletterTypeListResource"]
