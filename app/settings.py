"""Flask settings module."""
import os

from flask import Flask

from app.health import HEALTH_BLUEPRINT
from utils import db, migrate

app = Flask(__name__)

# Database settings.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Flask-SQLAlchemy.
db.init_app(app)

# Initialize Flask-Migrate.
migrate.init_app(app, db)

# Register blueprints.
app.register_blueprint(HEALTH_BLUEPRINT)

__all__ = ["app"]
