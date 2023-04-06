"""Async tasks definitions module."""
from celery import shared_task
from flask_mail import Message

from app.contact import Contact
from app.newsletter import Newsletter
from app.template import Template
from utils import mail


@shared_task
def mailer(id: str, params: object):
    """Build an email using a given newsletter ID.

    Parameters
    ----------
    id : str
        Newsletter ID which the information will come from.
    params : object
        Query params sended to the `/v1/newsletter/<id>/submissions` endpoint.

    """
    # TODO: find a way to make a cleaner solution for this algorithm.
    newsletter = Newsletter.find_by_id(id)

    try:
        mail_body = ""
        if newsletter.template_id is not None:
            mail_body = Template.find_by_id(newsletter.template_id).content

        if params.get("email") is not None:
            contacts = [params.get("email")]
        elif params.get("bulk_id") is not None:
            # TODO: add SELECT option to find_by_bulk_id method.
            contacts = [
                x.email for x in Contact.find_by_bulk_id(params.get("bulk_id"))
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
            msg.attach("attachment.png", "image/png", newsletter.attachment)

        mail.send(msg)
    except Exception as e:
        print(e)


__all__ = ["mailer"]
