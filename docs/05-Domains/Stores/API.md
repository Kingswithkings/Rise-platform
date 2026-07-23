# Stores API Design

## Public Endpoints

- `GET /stores`
- `GET /stores/{id}`
- `GET /stores/slug/{slug}`
- `GET /stores/search`

## Seller Endpoints

- `POST /stores`
- `PATCH /stores/{id}`
- `DELETE /stores/{id}`
- `GET /stores/me`
- `POST /stores/logo`
- `POST /stores/cover`

## Admin Endpoints

- `POST /stores/{id}/verify`
- `POST /stores/{id}/publish`
- `POST /stores/{id}/suspend`

## Authentication

Seller and admin endpoints require JWT Bearer authentication.

Admin endpoints require administrator authorization.

## Swagger Verification Checklist

- Create a store.
- Update store details.
- Retrieve a store by ID.
- Retrieve by slug.
- List all stores.
- List only the current user's stores.
- Verify a store as admin.
- Suspend a store as admin.
