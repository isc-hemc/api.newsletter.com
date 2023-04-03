"""Database migrations (Alembic) declaration module."""
from flask_migrate import Migrate

migrate = Migrate()

__all__ = ["migrate"]
