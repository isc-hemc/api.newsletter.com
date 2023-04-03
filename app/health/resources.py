"""Health resources module."""
import json

from flask import Response
from flask_restful import Resource


class HealthResource(Resource):
    """Extends from `Resource` and validates the current status of the API.

    Methods
    -------
    get()
        Retrieve an HTTP 200 status code with a health message.

    """

    def get(self) -> Response:
        """Retrieve an HTTP 200 status code with a health message.

        Returns
        -------
        Response
            HTTP success `Response` if the server is up and running.

        """
        return Response(
            json.dumps({"status": "Ok!"}),
            status=200,
            headers={"Content-Type": "application/json"},
        )


__all__ = ["HealthResource"]
