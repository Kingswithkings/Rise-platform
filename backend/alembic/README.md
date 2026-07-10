# Alembic

Alembic owns PostgreSQL schema history. Generate reviewed migrations from SQLAlchemy
metadata and never rewrite a migration that has been deployed.

```bash
docker compose run --rm backend alembic upgrade head
```
