#!/usr/bin/env bash

set -e

env=${FLASK_ENV:-production}
main=${FLASK_APP:-run.py}

if [ "$env" = "production" ]; then
  exec "$@"
else
#  flask run
  python3 -u $FLASK_APP
fi