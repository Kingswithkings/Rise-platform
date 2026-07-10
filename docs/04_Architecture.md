# Architecture

RISE is a modular monolith with independently deployable web and API applications.

## Backend boundaries

Each domain module follows:

`route → service → repository → database`

- Routes own transport validation and serialization.
- Services own business rules.
- Repositories own persistence queries.
- Schemas define API contracts; ORM models define persistence.

## Frontend boundaries

- `app/` owns routing and page composition.
- `features/` owns domain UI and feature logic.
- `components/` contains shared presentation.
- `services/` owns external API access.

## Runtime

Docker Compose starts PostgreSQL and Redis before FastAPI. The backend applies Alembic
migrations and idempotent seed data before serving requests. Next.js starts after the API
is healthy.
