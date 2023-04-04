"""Newsletter resources module."""
from flask import request
from flask_mail import Message
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from app.contact import Contact
from app.template import Template
from utils import mail

from .models import Newsletter
from .schemas import NewsletterSchema


class NewsletterResource(Resource):
    """Manage newsletter operations.

    Attributes
    ----------
    schema : NewsletterSchema
        Serialization schema object.

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

        try:
            newsletter = Newsletter(**serialized_data)
            newsletter.save()
        except:
            return {
                "message": "An error occurred during CREATE operation."
            }, 500

        try:
            mail_body = ""

            if newsletter.template_id is not None:
                template = Template.find_by_id(newsletter.template_id)
                mail_body = template.content

            contacts = Contact.find_all()

            msg = Message(
                serialized_data["subject"],
                recipients=[x.email for x in contacts],
                html=mail_body,
            )

            mail.send(msg)
        except:
            return {"message": "Mail server: connection refused."}, 502

        return self.schema.dump(newsletter), 201


__all__ = ["NewsletterResource"]
