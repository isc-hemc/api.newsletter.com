"""Bulk resources module."""
import csv
import io

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.contact import Contact
from app.subscription import Subscription
from utils import db

from .models import Bulk
from .schemas import BulkSchema


class BulkResource(Resource):
    """Manage single bulk resources.

    Attributes
    ----------
    schema : BulkSchema
        Serialization schema object.

    Methods
    -------
    post()
        Create a bulk of contact registries and store the bulk history.

    """

    schema = BulkSchema()

    def post(self):
        """Create a bulk of contact registries and store the bulk history."""
        data = request.form.to_dict()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        file = request.files.get("csv")
        if file is None:
            return {"csv": ["Missing data for required field."]}, 400

        bulk = Bulk.find_by_name(serialized_data["name"])
        if bulk is not None:
            return {
                "message": f"A registry with the name '{bulk.name}' already exists."
            }, 403

        try:
            bulk = Bulk(**serialized_data)
            bulk.save()
        except:
            return {
                "message": "An error occurred during CREATE operation."
            }, 500

        # TODO: move the following code to an async task.
        # TODO: find a way to make a cleaner solution for this algorithm.

        reader = csv.reader(io.TextIOWrapper(file))
        next(reader)

        for name, last_name, email in reader:
            try:
                contact = Contact(
                    name=name,
                    last_name=last_name,
                    email=email,
                    bulk_id=bulk.id,
                )
                subscriptions = Subscription.find_all()
                for sub in subscriptions:
                    contact.contacts_subscriptions.append(sub)
                contact.save()
            except:
                db.session.rollback()
                setattr(bulk, "errors", bulk.errors + 1)
                bulk.update()

        try:
            contacts = Contact.find_by_bulk_id(bulk.id)
            setattr(bulk, "inserted", contacts.count())

            bulk.update()
        except Exception as e:
            pass

        return self.schema.dump(bulk), 202


class BulkListResource(Resource):
    """Manage a list of bulk.

    Attributes
    ----------
    schema : BulkSchema
        Serialization schema object.

    Methods
    -------
    get()
        Retrieve a list of serialized bulks.

    """

    schema = BulkSchema(many=True)

    def get(self):
        """Retrieve a list of serialized bulks."""
        data = Bulk.find_all()

        serialized_data = self.schema.dump(data)

        return {"results": serialized_data}, 200


__all__ = ["BulkResource", "BulkListResource"]
