"""Newsletter resources module."""
from flask import Response, request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import DataError

from app.tasks import mailer

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

        params = request.args.to_dict()

        mailer.apply_async(args=[id, params])

        return Response(status=202)


__all__ = ["NewsletterResource", "NewsletterSubmissionResource"]
