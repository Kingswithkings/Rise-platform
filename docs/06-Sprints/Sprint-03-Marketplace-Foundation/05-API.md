# Sprint 03 API Scope

## Categories

- `POST /categories`
- `GET /categories`
- `GET /categories/tree`
- `GET /categories/{category_id}`
- `PATCH /categories/{category_id}`
- `DELETE /categories/{category_id}`

## Stores

### Public

- `GET /stores`
- `GET /stores/{id}`
- `GET /stores/slug/{slug}`
- `GET /stores/search`

### Seller

- `POST /stores`
- `PATCH /stores/{id}`
- `DELETE /stores/{id}`
- `GET /stores/me`

### Admin

- `POST /stores/{id}/verify`
- `POST /stores/{id}/publish`
- `POST /stores/{id}/suspend`
