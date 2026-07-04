#!/bin/sh
set -eu

alembic upgrade head
python -m app.database.seed
if [ "${APP_RELOAD:-false}" = "true" ]; then
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
fi
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
