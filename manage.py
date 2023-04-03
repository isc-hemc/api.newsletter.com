"""Project's command-line utility module."""
from flask import Flask

from app.health import HEALTH_BLUEPRINT

app = Flask(__name__)

app.register_blueprint(HEALTH_BLUEPRINT)
