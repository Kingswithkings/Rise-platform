# RISE-003 — Stores Engineering Pack

## Objective

Enable verified sellers to create and manage professional online stores.

## Business Value

Stores are the heart of the RISE marketplace. Products and services belong to stores, allowing sellers to operate a professional marketplace presence.

## Scope

### Database

- `stores`
- `store_documents`
- `store_images`
- `store_hours`

### Backend

- `models.py`
- `schemas.py`
- `repository.py`
- `service.py`
- `router.py`
- `validators.py`
- `README.md`
- `tests/`

### APIs

Public:

- `GET /stores`
- `GET /stores/{id}`
- `GET /stores/slug/{slug}`
- `GET /stores/search`

Seller:

- `POST /stores`
- `PATCH /stores/{id}`
- `DELETE /stores/{id}`
- `GET /stores/me`
- `POST /stores/logo`
- `POST /stores/cover`

Admin:

- `POST /stores/{id}/verify`
- `POST /stores/{id}/publish`
- `POST /stores/{id}/suspend`

## Store Lifecycle

```text
Draft
↓
Pending Review
↓
Verified
↓
Published
↓
Suspended
```

Only `Published` stores should be visible in public search.

## Swagger Verification

- Create a store.
- Update store details.
- Retrieve a store by ID.
- Retrieve by slug.
- List all stores.
- List only the current user's stores.
- Verify a store as admin.
- Suspend a store as admin.

## Completion Checklist

- [x] SQLAlchemy models
- [ ] Alembic migration
- [x] Pydantic schemas
- [x] Repository
- [x] Service
- [x] Router
- [x] Authentication
- [x] Seller authorization
- [x] Store validation
- [ ] Swagger tests
- [x] Unit tests
- [x] README
- [x] Sprint documentation
- [ ] Git commit

## Private Alpha Relevance

For private alpha, users must be able to:

- Register and log in
- Become a seller
- Create a verified store
- Add products
- Add services
- Browse categories
- Search the marketplace
- View trust badges
- Contact sellers

## Status

Not Started
