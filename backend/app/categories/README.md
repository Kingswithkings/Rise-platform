# Categories Domain

## Purpose

The Categories domain manages hierarchical classification across the RISE marketplace.

Categories support products, services, stores, search, navigation, analytics, and future AI recommendations.

## Architecture

The domain follows:

Router → Service → Repository → Database

## Database

Table: `categories`

The `parent_id` foreign key references another category and supports unlimited hierarchy depth.

## Public Endpoints

- `GET /categories`
- `GET /categories/tree`
- `GET /categories/{category_id}`

## Administrative Endpoints

- `POST /categories`
- `PATCH /categories/{category_id}`
- `DELETE /categories/{category_id}`

## Business Rules

- Category slugs must be globally unique.
- A category may have one parent.
- Root categories have no parent.
- A category cannot be its own parent.
- Circular hierarchies are prohibited.
- Categories are soft-deactivated rather than permanently deleted.
- A category with active children cannot be deactivated first.
- Category administration requires an administrator account.

## Future Work

- Product and service assignment validation
- Category translations
- Country-specific categories
- Category images
- Search indexing
- AI classification
