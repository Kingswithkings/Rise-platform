# Stores Domain

## Purpose

The Stores domain manages seller storefronts in the RISE marketplace.

A store is the primary business presence for a seller. Products and services belong to stores, not directly to users.

## Business Objective

Allow a verified seller to create and manage one or more stores.

## Responsibilities

- Create stores
- Update store profiles
- Manage store branding
- Connect stores to categories and geography
- Track verification status
- Integrate with 1stKings Trust
- Support future products and services
- Support future marketplace search

## Architecture

The domain follows:

Router → Service → Repository → Database

## Database

Tables:

- `stores`
- `store_documents`
- `store_images`
- `store_hours`

Core relationships:

- `owner_id` → `users.id`
- `category_id` → `categories.id`
- `country_id` → `countries.id`
- `city_id` → `cities.id`

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

## Business Rules

- Seller must be authenticated.
- Seller must have a completed profile.
- Seller must have a verified email.
- Seller must accept marketplace terms.
- Store slug must be globally unique.
- Store name is required.
- Category is required.
- Country is required.
- City is required.
- City must belong to the selected country.
- Address is required.
- Only published stores appear in public marketplace search.

## Store Status

- Draft
- Pending Review
- Verified
- Published
- Suspended

## Trust Integration

When a store is created, its initial trust score is `50`.

Future trust score increases will come from:

- Email verification
- Phone verification
- Business verification
- Positive reviews
- Successful orders

## Future Integrations

- Products
- Services
- Orders
- Reviews
- Trust
- Analytics
- AI Assistant
- Payments
- Shipping
- Notifications

## Future AI Opportunities

- AI-generated store descriptions
- AI-generated SEO titles
- AI keyword suggestions
- AI product recommendations
- AI pricing insights
- AI sales analytics
