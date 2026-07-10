# RISE Platform

Global AI-powered Marketplace & Services Platform.

## Technology

- FastAPI
- Next.js
- PostgreSQL
- Redis
- Docker
- React Native
- OpenAI

## Quick start

Prerequisites: Docker Engine with Docker Compose v2.

```bash
docker compose up
```

Services:

- Web: http://localhost:3000
- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- API health: http://localhost:8000/health
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

The API container waits for PostgreSQL, applies Alembic migrations, loads idempotent seed
data, and then starts FastAPI. Seed data includes six geographic regions, the initial
14 launch/expansion countries, and an administrator configured through `SEED_ADMIN_EMAIL`
and `SEED_ADMIN_PASSWORD`.

## Development

```bash
make test
make lint
docker compose down -v
```

Architecture and contribution rules are documented in
[docs/04_Architecture.md](docs/04_Architecture.md) and
[docs/09_Development_Process.md](docs/09_Development_Process.md).
Delivery and business operations are maintained in [management/](management/).
