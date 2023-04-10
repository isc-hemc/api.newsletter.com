"""Async tasks definitions module."""
from celery import shared_task
from flask_mail import Message

from app.contact import Contact
from app.newsletter import Attachment, Newsletter
from app.subscription import Subscription
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
                x for x in Contact.find_by_bulk_id(params.get("bulk_id"))
            ]
        else:
            # TODO: add SELECT option to find_all method.
            contacts = [x for x in Contact.find_all()]

        # TODO: perform this operation in SQL.
        recipients = []
        for x in contacts:
            sub = Subscription.query.filter_by(
                newsletter_type_id=newsletter.newsletter_type_id,
                contact_id=x.id,
            ).first()
            if sub.is_active:
                recipients.append(x)

        for x in recipients:
            msg = Message(
                newsletter.subject,
                recipients=[x.email],
                html=mail_body.replace("{{id}}", str(x.id)),
            )

            if newsletter.attachment_id is not None:
                attachment = Attachment.find_by_id(newsletter.attachment_id)
                msg.attach(
                    attachment.name, attachment.mimetype, attachment.file
                )

            mail.send(msg)
    except Exception as e:
        print(e)


__all__ = ["mailer"]
