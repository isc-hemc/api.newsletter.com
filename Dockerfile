FROM python:3.10 as python-base

ENV HOME=/opt/api

RUN apt-get -y update && mkdir $HOME

WORKDIR $HOME

FROM python-base as builder

COPY app ./app
COPY utils ./utils
COPY manage.py Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install

CMD [ "pipenv", "run", "dev" ]
