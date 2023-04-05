"""Newsletter resources module."""
from flask import request
from flask_mail import Message
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import DataError

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
        Create a new registry.

    """

    schema = NewsletterSchema()

    def post(self):
        """Create a new registry."""
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

        return self.schema.dump(newsletter), 201


class NewsletterSubmissionResource(Resource):
    """Manage newsletter's mailing operations.

    Methods
    -------
    get(id: str)
        Retrieve a newsletter registry and send it to a recipient list.

    """

    def get(self, id: str):
        """Retrieve a newsletter registry and send it to a recipient list."""
        try:
            newsletter = Newsletter.find_by_id(id)
        except DataError:
            return {
                "message": f"The parameter '{id}' is not a valid UUID."
            }, 400

        if newsletter is None:
            return {"message": f"Newsletter with ID '{id}' not found."}, 404

        try:
            mail_body = ""

            if newsletter.template_id is not None:
                mail_body = Template.find_by_id(newsletter.template_id).content

            msg = Message(
                newsletter.subject,
                recipients=[x.email for x in Contact.find_all()],
                html=mail_body,
            )

            mail.send(msg)
        except:
            return {"message": "Mail server: connection refused."}, 502

        return {"message": "Newsletter sent!"}, 202


__all__ = ["NewsletterResource", "NewsletterSubmissionResource"]
