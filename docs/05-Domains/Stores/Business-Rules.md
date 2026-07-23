# Stores Business Rules

## Seller Rules

- Seller must be authenticated.
- Seller must have the Seller role.

## Store Rules

- Store slug must be globally unique.
- Store name is required.
- Category is required.
- Country is required.
- City is required.
- City must belong to the selected country.
- Address is required.
- Email should be validated.
- Latitude and longitude are optional but recommended for location-based search.
- Stores are soft-deactivated rather than permanently deleted.
- Only published stores appear in public marketplace search.

## Trust Rules

- A store starts with Trust Score `50`.
- Trust will later increase with email verification, phone verification, business verification, positive reviews, and successful orders.

## Status Rules

Supported statuses:

- Draft
- Pending Review
- Verified
- Published
- Suspended
