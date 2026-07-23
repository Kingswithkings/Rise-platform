# ADR-012

## Title

Separate Core and Common Backend Components

## Status

Accepted

## Context

RISE will add many domains: Stores, Products, Services, Reviews, Search, Orders, Payments, AI, Notifications, Analytics, and Media.

These domains need shared functionality, but framework-level primitives and reusable domain-support utilities have different responsibilities.

## Decision

Use:

- `app/core` for framework-level backend primitives.
- `app/common` for reusable domain-support components.

## Core Responsibilities

- Configuration
- Security
- Authentication helpers
- Exception handling
- Logging
- Pagination
- API response helpers

## Common Responsibilities

- Base SQLAlchemy model
- Base repository
- Base service
- Validators
- Slug generation
- File upload utilities

## Consequences

- Shared code has clear ownership.
- Domain packages stay focused on business capability.
- Core and Common must remain free of feature-specific business logic.
