# Testing Strategy

## Test levels

- Unit tests cover business rules.
- API tests cover contracts and failure behavior.
- Integration tests cover PostgreSQL, Redis, migrations, and seeds.
- Frontend tests cover components and service clients.
- Playwright covers critical user journeys.
- Docker Compose smoke tests validate the deployable system.

Tests must be deterministic and run in CI. A regression fix requires a reproducing test
where practical.
