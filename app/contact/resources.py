"""Contact resources module."""
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from app.subscription import Subscription

from .models import Contact
from .schemas import ContactSchema


class ContactResource(Resource):
    """Manage single contact resources.

    Attributes
    ----------
    schema : ContactSchema
        Contact serialization schema object.

    Methods
    -------
    post()
        Create a new contact registry.

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
                "message": f"A registry with the email '{data['email']}' already exists."
            }, 403

        try:
            contact = Contact(**serialized_data)
            subscriptions = Subscription.find_all()
            for sub in subscriptions:
                contact.contacts_subscriptions.append(sub)
            contact.save()
        except:
            return {"message": "An error occurred while saving the data."}, 409

        return self.schema.dump(contact), 201


class ContactListResource(Resource):
    """Manage a list of contacts.

    Methods
    -------
    get()
        Retrieve a list of serialized contacts.

    """

    schema = ContactSchema(many=True)

    def get(self):
        """Retrieve a list of serialized contacts."""
        data = Contact.find_all()

        serialized_data = self.schema.dump(data)

        return {"results": serialized_data}, 200


__all__ = ["ContactResource", "ContactListResource"]
