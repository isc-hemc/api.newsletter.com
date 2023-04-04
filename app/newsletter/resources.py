"""Newsletter resources module."""
from flask import request
from flask_mail import Message
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from app import Contact
from utils import mail

from .models import Newsletter
from .schemas import NewsletterSchema


class NewsletterResource(Resource):
    """Manage newsletter operations.

    Attributes
    ----------
    schema : NewsletterSchema
        Newsletter serialization schema object.

    Methods
    -------
    post()
        Create a newsletter registry and send it to a recipients list.

    """

    schema = NewsletterSchema()

    def post(self):
        """Create a newsletter registry and send it to a recipients list."""
        data = request.get_json()

        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        contacts = Contact.find_all()

        msg = Message(
            serialized_data["subject"], recipients=[x.email for x in contacts]
        )

        try:
            mail.send(msg)
        except:
            return {"message": "Mail server: connection refused."}, 502

        try:
            newsletter = Newsletter(**serialized_data)
            newsletter.save()
        except:
            return {"message": "An error occurred while saving the data."}, 409

        return self.schema.dump(newsletter), 201


__all__ = ["NewsletterResource"]
