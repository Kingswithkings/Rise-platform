# Architecture

RISE is a modular monolith with independently deployable web and API applications.

## Backend boundaries

Each domain module follows this dependency flow:

`route → service → repository → database`

- Routes validate transport input, call a service, and serialize output.
- Services contain business rules and depend on repository protocols.
- Repositories own all database queries.
- Schemas define API contracts; ORM models define persistence.

Business logic and direct database access are prohibited in routes. Public functions and
data structures are typed. Every domain module must add tests and update documentation.

## Frontend boundaries

- `app/` owns routing and page composition.
- `features/` owns domain UI and feature logic.
- `components/` contains shared presentation components.
- `services/` owns external API access.
- `store/`, `providers/`, `hooks/`, and `types/` contain shared typed infrastructure.

## Runtime

Docker Compose starts PostgreSQL and Redis first. After both health checks pass, FastAPI
runs migrations and seed data. Next.js starts only after the API becomes healthy.
