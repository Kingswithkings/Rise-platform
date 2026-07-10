# Coding Standards

## Backend

- Python 3.12 with complete public-interface type annotations
- SQLAlchemy 2.x typed mappings
- Feature modules following route, service, repository, schema, and model boundaries
- Ruff and Black enforced in CI

## Frontend

- TypeScript with strict checking
- Feature-owned components and logic
- Shared components remain domain-neutral
- ESLint and Prettier enforced in CI

Prefer small, explicit modules over speculative abstractions.
