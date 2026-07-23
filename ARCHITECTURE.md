# RISE Architecture

## Architecture Style

RISE uses a modular monolith architecture with FastAPI.

Each business domain owns its models, schemas, repository, service, router, validators, tests, and README.

## Backend Domain Structure

```text
backend/app/<domain>/
├── README.md
├── models.py
├── schemas.py
├── repository.py
├── service.py
├── router.py
├── validators.py
└── tests/
```

## Current Domains

- Authentication
- Users
- Geography
- 1stKings Trust
- Categories
- Stores

## Planned Domains

- Products
- Services
- Reviews
- Media
- Search
- Favorites
- Messaging
- Notifications
- Orders
- Payments
- AI
- Analytics

## Shared Components

- `app/core` — framework-level primitives
- `app/common` — reusable domain-support components

## Principle

Extract services only when there is a proven operational, scaling, or ownership reason.
