# Deployment

Docker is the deployment unit for the Next.js frontend and FastAPI backend. PostgreSQL
and Redis are required runtime dependencies.

## Local startup

```bash
docker compose up --build
```

The backend entrypoint applies migrations and seed data before starting the API. CI builds
both images and runs a full-stack health and seed-data acceptance check.
