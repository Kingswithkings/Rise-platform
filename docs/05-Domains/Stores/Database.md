# Stores Database Design

## Goal

Use a normalized store design instead of storing all store data in one large table.

## Tables

- `stores`
- `store_documents`
- `store_images`
- `store_hours`

## `stores`

Primary seller storefront table.

### Columns

- `id`
- `owner_id`
- `category_id`
- `country_id`
- `city_id`
- `store_name`
- `slug`
- `description`
- `logo_url`
- `cover_url`
- `email`
- `phone`
- `website`
- `address`
- `latitude`
- `longitude`
- `status`
- `verified`
- `active`
- `trust_score`
- `average_rating`
- `created_at`
- `updated_at`

### Lifecycle

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

### Foreign Keys

- `owner_id` → `users.id`
- `category_id` → `categories.id`
- `country_id` → `countries.id`
- `city_id` → `cities.id`

### Indexes

- Unique index on `slug`
- Index on `owner_id`
- Index on `category_id`
- Index on `country_id`
- Index on `city_id`
- Index on `status`
- Index on `verified`
- Index on `active`

## `store_documents`

Stores business verification documents.

### Columns

- `id`
- `store_id`
- `document_type`
- `file_url`
- `status`
- `created_at`
- `updated_at`

### Foreign Keys

- `store_id` → `stores.id`

## `store_images`

Stores logo, cover image, and future gallery images.

### Columns

- `id`
- `store_id`
- `image_type`
- `image_url`
- `alt_text`
- `sort_order`
- `active`
- `created_at`
- `updated_at`

### Foreign Keys

- `store_id` → `stores.id`

## `store_hours`

Stores opening hours.

### Columns

- `id`
- `store_id`
- `day_of_week`
- `opens_at`
- `closes_at`
- `closed`
- `created_at`
- `updated_at`

### Foreign Keys

- `store_id` → `stores.id`
