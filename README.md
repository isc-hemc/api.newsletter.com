# api.newsletter.com

REST API for storicard challenge, a simple newsletter app.

## Contents

-   [Dependencies](#dependencies)
-   [Configuration](#configuration)
-   [Run](#run)
-   [Authors](#authors)

## Dependencies

![Python +3.10](https://img.shields.io/badge/Python-+3.10-blue.svg)
![Celery +5.2](https://img.shields.io/badge/Celery-+5.2-green.svg)
![PostgreSQL +15.0](https://img.shields.io/badge/PostgreSQL-+15.0-black.svg)
![Redis +6.2](https://img.shields.io/badge/Redis-+6.2-red.svg)
![Docker +20.10](https://img.shields.io/badge/Docker-+20.10-lightgrey.svg)

## Configuration

Create an **.env** based on the [.env.template](./.env.template):

```sh
cp .env.template .env
```

If you need to update any value here's the list of the environment variables definition:

| Variable                  | Default value                                                     | Description                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| CELERY_BROKER_URL         | redis://0.0.0.0:6379/0                                            | Default broker URL. If running broker using docker the default value points to the newsletter_broker container at its 0 db.                     |
| CELERY_RESULT_BACKEND_URL | redis://0.0.0.0:6379/1                                            | Default result backend URL. If running broker using docker the default value points to the newsletter_broker container at its 1 db.             |
| DATABASE_URL              | postgresql://postgres:iUFXkPr7\_!nm98EY@127.0.0.1:5432/newsletter | Database to which SQLAlchemy will connect to.                                                                                                   |
| FLASK_APP                 | manage.py                                                         | Project main module.                                                                                                                            |
| FLASK_DEBUG               | True                                                              | If `True` then the flask's debug mode will be activated.                                                                                        |
| MAIL_DEBUG                | True                                                              | If `True`, then the flask-mail debug model will be activated.                                                                                   |
| MAIL_DEFAULT_SENDER       | email@gmail.com                                                   | Default mail sender.                                                                                                                            |
| MAIL_PASSWORD             |                                                                   | If using gmail's SMTP server then this field should be supplied with an app password: <https://support.google.com/accounts/answer/185833?hl=es> |
| MAIL_PORT                 | 587                                                               | SMPT server port.                                                                                                                               |
| MAIL_SERVER               | smtp.gmail.com                                                    | SMTP server.                                                                                                                                    |
| MAIL_USERNAME             | email@gmail.com                                                   | Email related to the `MAIL_PASSWORD` env variable.                                                                                              |
| MAIL_USE_TLS              | True                                                              | Enable TLS protocol.                                                                                                                            |

## Run

The easiest and fastest way to run this project is through Docker, just open a terminal on the project's root and execute the following command:


```sh
docker-compose up --build -d
```

This command will build the following containers:
* PostgreSQL database
* Redis server (broker)
* Celery worker
* Flask API

At this point you should be able to perform requests to the URL: [http://0.0.0.0:8000/v1/](http://0.0.0.0:8000/v1/).

By using this methods, dependencies and migrations are automatically installed and executed respectively.

### Alternatives

If you would like to run the project without Docker, then:

> Install project dependencies:
```sh
pipenv install
```

> Execute migrations:
```sh
pipenv run migrate
```

> Run Flask API and Celery worker:
```sh
pipenv run dev
pipenv run tasks
```

## Authors

Carlos David Hernández Martínez - [Davestring](https://github.com/Davestring)
