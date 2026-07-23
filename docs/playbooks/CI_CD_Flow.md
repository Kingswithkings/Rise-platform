# CI/CD Flow

RISE deployments should follow this flow:

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

## Purpose

This catches issues early and keeps deployments consistent.

## Required Checks

- Backend lint
- Backend tests
- Frontend lint
- Frontend build
- Docker build
- Migration check
