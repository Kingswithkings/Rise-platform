# Backend Application

Feature packages own their routes, schemas, services, repositories, and models. Shared
infrastructure belongs in `core`, `database`, or `shared`; feature-specific behavior must
not leak into those packages.

## Recommended Domain Structure

```text
app/
├── core/
├── auth/
├── users/
├── geography/
├── trust/
├── categories/
├── stores/
├── products/
├── services/
├── reviews/
├── search/
├── orders/
├── payments/
├── ai/
├── notifications/
├── analytics/
├── media/
├── admin/
└── common/
```

## Core and Common Split

`app/core` contains framework-level backend primitives:

- Configuration
- Security
- Authentication helpers
- Exception handling
- Logging
- Pagination
- API response helpers

`app/common` is reserved for reusable domain-support components:

- Base SQLAlchemy model
- Base repository
- Base service
- Validators
- Slug generation
- File upload utilities
