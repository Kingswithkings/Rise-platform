# ADR-010

## Title

Shared Base Entity for Common Model Fields

## Status

Proposed

## Context

Many RISE domains require common fields such as `id`, `created_at`, `updated_at`, and `active`.

Categories, Stores, Products, Services, Orders, and Reviews all need consistent entity metadata.

## Decision

Introduce a shared SQLAlchemy mixin for common model fields before implementing the Stores domain.

## Alternatives

- Continue duplicating fields in every model.
- Use inheritance for all models instead of mixins.

## Reason

A shared mixin reduces duplication, keeps models consistent, and makes future schema conventions easier to maintain.

## Consequences

- Existing models may need gradual refactoring.
- Migrations must be reviewed carefully to avoid accidental schema changes.
- The mixin should be introduced without changing existing table definitions unless explicitly required.
