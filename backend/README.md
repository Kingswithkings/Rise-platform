# Backend

## Purpose

The backend provides the versioned RISE API, business rules, persistence, authentication,
health checks, migrations, and seed operations.

## Architecture

RISE uses a modular monolith. Feature modules follow:

`route → service → repository → database`

## Run locally

From the repository root:

```bash
docker compose up --build backend
```

Swagger is available at `http://localhost:8000/docs`.

## Folder layout

- `app/` — application and feature modules
- `alembic/` — database migrations
- `tests/` — backend automated tests
- `requirements/` — production and development dependencies
- `scripts/` — container entrypoints and backend automation

## Coding standards

Use Python 3.12, typed interfaces, SQLAlchemy 2.x mappings, repository-owned queries, and
idempotent seeds. Ruff, Black, and Pytest are required quality gates.
