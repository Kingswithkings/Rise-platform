# ADR-011

## Title

Introduce Core Module for Shared Backend Primitives

## Status

Accepted

## Context

RISE domains share common backend requirements such as base model fields, repository helpers, pagination, common responses, exceptions, security helpers, utilities, and validators.

Without a shared Core module, these concerns will be duplicated across Categories, Stores, Products, Services, Orders, and Reviews.

## Decision

Create `app/core/` as the home for shared backend primitives.

Initial files:

- `base_model.py`
- `base_repository.py`
- `exceptions.py`
- `pagination.py`
- `responses.py`
- `security.py`
- `utils.py`
- `validators.py`

## Alternatives

- Keep duplicating shared code inside each domain.
- Introduce shared utilities later after more duplication exists.

## Consequences

- New domains can reuse consistent primitives.
- Existing domains can be migrated gradually.
- Core must remain domain-neutral and must not contain marketplace business rules.
