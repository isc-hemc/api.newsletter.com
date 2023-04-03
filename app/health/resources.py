"""Health resources module."""
import json

from flask_restful import Resource


class HealthResource(Resource):
    """Extends from `Resource` and validates the current status of the API.

    Methods
    -------
    get()
        Retrieve an HTTP 200 status code with a health message.

    """

    def get(self):
        """Retrieve an HTTP 200 status code with a health message."""
        return {"status": "Ok!"}, 200


__all__ = ["HealthResource"]
