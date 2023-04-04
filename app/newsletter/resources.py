"""Newsletter resources module."""
from smtplib import SMTPAuthenticationError

from flask_mail import Message
from flask_restful import Resource

from utils import mail


class NewsletterResource(Resource):
    """Manage newsletter operations.

    Methods
    -------
    post()
        Create a newsletter registry and send it to a recipients list.

    """

    def post(self):
        """Create a newsletter registry and send it to a recipients list."""
        msg = Message("Testing mail service!", recipients=[""])

        try:
            mail.send(msg)
        except ConnectionRefusedError:
            return {"message": "Mail server: connection refused."}, 502
        except SMTPAuthenticationError as e:
            return {
                "message": "Mail server: invalid username or password."
            }, 401

        return {"message": "Email sended!"}, 202


__all__ = ["NewsletterResource"]
