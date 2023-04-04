"""Flask settings module."""
import os

from flask import Flask
from flask_cors import CORS

from app import CONTACT_BLUEPRINT, HEALTH_BLUEPRINT, NEWSLETTER_BLUEPRINT
from utils import db, ma, mail, migrate

app = Flask(__name__)

# Enable CORS support on all routes.
CORS(app)

# Database settings.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Flask-SQLAlchemy.
db.init_app(app)

# Initialize Flask-Marshmallow.
ma.init_app(app)

# Initialize Flask-Migrate.
migrate.init_app(app, db)

# Initialize Flask-Mail
app.config["MAIL_DEBUG"] = os.environ.get("MAIL_DEBUG") == "True"
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT", 587)
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS") == "True"
mail.init_app(app)

# Register blueprints.
app.register_blueprint(CONTACT_BLUEPRINT)
app.register_blueprint(HEALTH_BLUEPRINT)
app.register_blueprint(NEWSLETTER_BLUEPRINT)

__all__ = ["app"]
