"""Database instance declaration module."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = ["db"]
