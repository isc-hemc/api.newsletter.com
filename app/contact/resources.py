"""Contact resources module."""
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from app.newsletter_type import NewsletterType
from app.subscription import Subscription, SubscriptionSchema
from utils import ListResource

from .models import Contact
from .schemas import ContactSchema


class ContactResource(Resource):
    """Manage single contact resources.

    Attributes
    ----------
    schema : ContactSchema
        Serialization schema object.

    Methods
    -------
    post()
        Create a new registry.

    """

    schema = ContactSchema()

    def post(self):
        """Create a new contact registry."""
        data = request.get_json()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        contact = Contact.find_by_email(serialized_data["email"])
        if contact is not None:
            return {
                "message": f"A registry with the email '{contact.email}' already exists."
            }, 403

        try:
            contact = Contact(**serialized_data)
            contact.save()

            newsletter_types = NewsletterType.find_all()
            for newsletter_type in newsletter_types:
                subscription = Subscription(
                    contact_id=contact.id,
                    newsletter_type_id=newsletter_type.id,
                    is_active=True,
                )
                subscription.save()
        except:
            return {
                "message": "An error occurred during CREATE operation."
            }, 500

        return self.schema.dump(contact), 201


class ContactListResource(ListResource):
    """Extends from `ListResource` and manage a list of contacts."""

    model = Contact
    schema_class = ContactSchema


class ContactSubscriptionResource(Resource):
    """Manage subscriptions related to a contact.

    Attributes
    ----------
    schema : SubscriptionSchema
        Serialization schema object.

    Methods
    -------
    patch()
        Update an existing subscription registry.

    """

    schema = SubscriptionSchema()

    def patch(self, **kwargs):
        """Update an existing subscription registry."""
        subscription = Subscription.query.get_or_404(kwargs["subscription_id"])

        data = request.get_json()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        try:
            setattr(subscription, "is_active", serialized_data["is_active"])
            subscription.update()
        except Exception as e:
            return {
                "message": "An error occurred during PATCH operation."
            }, 500

        return self.schema.dump(subscription), 200


class ContactSubscriptionListResource(Resource):
    """Manage a list of subscriptions related to a contact.

    Attributes
    ----------
    schema : SubscriptionSchema
        Serialization schema object.

    Methods
    -------
    get()
        Retrive a list of subscriptions related to a contact.

    """

    schema = SubscriptionSchema(many=True)

    def get(self, **kwargs):
        """Retrive a list of subscriptions related to a contact."""
        subscriptions = Subscription.query.filter_by(**kwargs)

        serialized_data = self.schema.dump(subscriptions)

        return {"results": serialized_data}, 200


__all__ = [
    "ContactResource",
    "ContactListResource",
    "ContactSubscriptionResource",
    "ContactSubscriptionListResource",
]
