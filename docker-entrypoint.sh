#!/bin/bash

pipenv run migrate

exec "$@"
