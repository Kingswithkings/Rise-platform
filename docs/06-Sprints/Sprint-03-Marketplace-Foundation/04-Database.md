# Sprint 03 Database Changes

## Categories

- `categories`

## Stores

Planned tables:

- `stores`
- `store_images`
- `store_hours`
- `store_documents`

## Stores Relationships

- `users` 1 → many `stores`
- `categories` 1 → many `stores`
- `countries` 1 → many `stores`
- `cities` 1 → many `stores`
- `stores` 1 → many `products`
- `stores` 1 → many `services`

## Store Visibility Rule

Only `Published` stores should be visible in public search.
