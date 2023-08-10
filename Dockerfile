FROM python:3.12.0b4-slim as python-base

ENV HOME=/opt/api

RUN apt-get -y update && mkdir $HOME

WORKDIR $HOME

FROM python-base as builder

COPY app ./app
COPY migrations ./migrations
COPY utils ./utils
COPY manage.py Pipfile Pipfile.lock docker-entrypoint.sh ./

RUN pip install pipenv
RUN pipenv install

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD [ "pipenv", "run", "dev" ]
