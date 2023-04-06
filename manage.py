"""Project's command-line utility module."""
from app import app, init_celery

celery_app = init_celery(app)
