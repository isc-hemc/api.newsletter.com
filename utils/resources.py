"""Utility resources module."""
from flask import request
from flask_restful import Resource


class ListResource(Resource):
    """Manage GET list requests.

    Attributes
    ----------
    model : SQLAlchemy.Model
        Model to which operations will be made.
    schema_class : Marshmallow.SQLAlchemyAutoSchema
        Schema class for serialize/deserialize the `model` results.

    Methods
    -------
    _get_model()
        Raise an exception if `model` attribute is not specified.
    _get_queryset()
        Retrieve all (or filter) the `model` registries.
    _get_schema_class()
        Raise an exception if `schema_class` attribute is not specified.
    _get_schema()
        Returns an instance of `schema_class`.
    get()
        Retrive a list of registries related to `model`.

    """

    model = None
    schema_class = None

    def _get_model(self):
        """Raise an exception if `model` attribute is not specified."""
        assert self.model is not None, "Include the `model` attribute."
        return self.model

    def _get_queryset(self):
        """Retrieve all (or filter) the `model` registries."""
        model = self._get_model()

        args = request.args.to_dict()
        if args:
            return model.query.filter_by(**args)

        return model.query.all()

    def _get_schema_class(self):
        """Raise an exception if `schema_class` attribute is not specified."""
        assert (
            self.schema_class is not None
        ), "Include the `schema_class` attribute."
        return self.schema_class

    def _get_schema(self, *args, **kwargs):
        """Return an instance of `schema_class`."""
        schema_class = self._get_schema_class()
        return schema_class(*args, **kwargs)

    def get(self):
        """Retrive a list of registries related to `model`."""
        queryset = self._get_queryset()

        schema = self._get_schema(many=True)

        return {"results": schema.dump(queryset)}, 200


__all__ = ["ListResource"]
