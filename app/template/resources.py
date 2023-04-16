"""Template resources module."""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from utils import ListResource

from .models import Template
from .schemas import TemplateSchema


class TemplateResource(Resource):
    """Manage single template resources.

    Attributes
    ----------
    schema : TemplateSchema
        Serialization schema object.

    Methods
    -------
    post()
        Create a new registry.

    """

    schema = TemplateSchema()

    def post(self):
        """Create a new registry."""
        data = request.get_json()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        template = Template.find_by_name(serialized_data["name"])
        if template is not None:
            return {
                "message": f"A registry with the name '{template.name}' already exists."
            }, 403

        try:
            template = Template(**serialized_data)
            template.save()
        except Exception as e:
            return {
                "message": "An error occurred during CREATE operation."
            }, 500

        return self.schema.dump(template), 201


class TemplateListResource(ListResource):
    """Extends from `ListResource` and manage a list of templates."""

    model = Template
    schema_class = TemplateSchema


__all__ = ["TemplateResource", "TemplateListResource"]
