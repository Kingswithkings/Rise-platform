# Development Process

Every sprint follows:

1. Sprint Planning
2. Architecture Review
3. Implementation
4. Testing
5. Code Review
6. Deployment
7. Sprint Demo
8. Retrospective

Branches and pull requests should reference a `RISE-###` task.

## Git workflow

- `main` is protected and deployable.
- Development changes are made on short-lived branches.
- Changes reach `main` through reviewed pull requests with required CI checks.
- Direct pushes and force pushes to `main` are prohibited.

## Definition of done

- Acceptance criteria are met.
- Types, tests, documentation, and migrations are included.
- Backend passes Ruff, Black, and Pytest.
- Frontend passes ESLint, Prettier, TypeScript, Vitest, and Playwright.
- API changes appear in Swagger.
- No secrets are committed.
