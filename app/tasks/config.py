"""Tasks config module."""
from celery import Celery, Task
from flask import Flask


def init_celery(app: Flask):
    """Celery init function.

    Parameters
    ----------
    app : Flask
        Flask application needed in order to sync its context to a celery app.

    Returns
    -------
    Celery
        Configured celery application.

    """

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery = Celery(app.name, task_cls=FlaskTask)
    celery.config_from_object(app.config["CELERY"])
    celery.set_default()
    app.extensions["celery"] = celery
    return celery


__all__ = ["init_celery"]
