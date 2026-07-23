# RISE Deployment

## Initial Deployment Direction

Recommended initial platforms:

- Render
- Azure App Service

## Runtime Components

- FastAPI backend
- Next.js frontend
- PostgreSQL
- Redis
- S3-compatible object storage for images

## CI/CD Flow

```text
Push
↓
Lint
↓
Unit Tests
↓
Integration Tests
↓
Build Docker
↓
Deploy to Staging
↓
Manual Approval
↓
Production
```

## Operational Baseline

- Structured logging
- Error tracking
- `/health`
- `/ready`
- Basic performance metrics
- Automated PostgreSQL backups
