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
        data = request.form.to_dict()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        attachment = None
        if request.files.get("attachment") is not None:
            attachment = request.files.get("attachment").read()

        try:
            newsletter = Newsletter(attachment=attachment, **serialized_data)
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

        # TODO: move the following code to an async task.
        # TODO: find a way to make a cleaner solution for this algorithm.

        try:
            mail_body = ""
            if newsletter.template_id is not None:
                mail_body = Template.find_by_id(newsletter.template_id).content

            params = request.args.to_dict()
            if params.get("email") is not None:
                contacts = [params.get("email")]
            elif params.get("bulk_id") is not None:
                # TODO: add SELECT option to find_by_bulk_id method.
                contacts = [
                    x.email
                    for x in Contact.find_by_bulk_id(params.get("bulk_id"))
                ]
            else:
                # TODO: add SELECT option to find_all method.
                contacts = [x.email for x in Contact.find_all()]

            msg = Message(
                newsletter.subject,
                recipients=contacts,
                html=mail_body,
            )

            if newsletter.attachment is not None:
                msg.attach(
                    "attachment.png", "image/png", newsletter.attachment
                )

            mail.send(msg)
        except Exception as e:
            return {"message": "Mail server: connection refused."}, 502

        return {"message": "Newsletter sent!"}, 202


__all__ = ["NewsletterResource", "NewsletterSubmissionResource"]
