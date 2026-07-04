# Development

## Workflow

Work moves from Epic → Feature → User Story → Task → Implementation → Testing → Review →
Deployment. Branches should reference a RISE task identifier.

## Definition of done

- Acceptance criteria are met.
- Types, tests, documentation, and migration changes are included.
- Backend code passes Ruff, Black, and Pytest.
- Frontend code passes ESLint, Prettier, TypeScript, Vitest, and Playwright.
- API changes are visible in Swagger.
- Secrets are not committed.

## Database changes

Create migrations from the backend container:

```bash
docker compose run --rm backend alembic revision --autogenerate -m "description"
docker compose run --rm backend alembic upgrade head
```

Seed operations must be idempotent. Never edit a migration that has been deployed.
