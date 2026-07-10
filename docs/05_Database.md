# Database

PostgreSQL is the system of record. SQLAlchemy 2.x defines persistence models and Alembic
manages schema evolution.

## Rules

- Every schema change requires a migration.
- Never edit a migration that has been deployed.
- Seed operations must be idempotent.
- Foreign keys and uniqueness constraints must enforce domain invariants.
- Application code accesses data through repositories.

Sprint 1 seeds six regions and fourteen initial launch or expansion countries.
