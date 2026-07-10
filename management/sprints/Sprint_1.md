# Sprint 1 — Production Foundation

## Goal

Create a repeatable production-oriented engineering foundation.

## Deliverables

- [x] Production repository
- [x] Engineering documentation
- [x] Docker environment
- [x] PostgreSQL
- [x] Redis
- [x] FastAPI
- [x] Next.js
- [x] Alembic
- [x] CI/CD workflows
- [x] Authentication scaffold
- [x] Region and country seed data
- [x] Developer guide
- [ ] Tailwind
- [ ] shadcn/ui
- [ ] Protected `main` branch
- [ ] Passing remote CI pipeline on the documentation pull request

## Daily engineering plan

### Day 1 — Repository Bootstrap

Repository, folder structure, documentation, README, and development standards.

### Day 2 — Infrastructure

Docker Compose, PostgreSQL, Redis, and environment variables.

### Day 3 — Backend

FastAPI, SQLAlchemy, Alembic, and structured logging.

### Day 4 — Frontend

Next.js, Tailwind, shadcn/ui, and authentication context.

### Day 5 — CI/CD

GitHub Actions, Ruff, ESLint, Pytest, and Playwright.

## Tasks

- RISE-001 Repository Bootstrap
- RISE-002 Docker and Development Environment
- RISE-003 PostgreSQL Foundation

## Progress

Core services, migrations, seeds, Swagger, and CI acceptance checks are operational.

## Geography Progress

- [x] Region model and API
- [x] Country model and API
- [x] City model and API
- [x] PostgreSQL migration
- [x] Swagger verification
- [ ] Automated tests
- [ ] Seed data

## Completed

- Next.js, FastAPI, PostgreSQL, and Redis run through Docker Compose.
- Database migrations and geographic seeds are applied.

## Blocked

- GitHub publishing and branch protection require an installed and authenticated `gh`.
- Tailwind and shadcn/ui require a scoped frontend implementation task.

## Lessons learned

Container health checks must use explicit interfaces and startup dependencies.

## Next sprint

Authentication and User Management.

## Exit criteria

A fresh clone must start with `docker compose up` and expose a working backend, frontend,
PostgreSQL, Redis, Swagger, current migrations, and loaded seed data. The remote CI
pipeline must pass.

## Weekly CTO review

- What did we build?
- What slowed us down?
- What technical debt did we create?
- What should we improve next sprint?
- Are we still aligned with the product vision?
