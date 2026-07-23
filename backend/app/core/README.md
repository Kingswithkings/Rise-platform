# Core Module

## Purpose

The Core module contains reusable backend primitives shared across RISE domains.

It should stay framework-level and domain-neutral.

## Responsibilities

- Base SQLAlchemy mixins
- Base repository helpers
- Common exceptions
- Pagination helpers
- Standard API responses
- Shared security helpers
- Utility functions
- Common validators

## Files

- `base_model.py`
- `base_repository.py`
- `exceptions.py`
- `pagination.py`
- `responses.py`
- `security.py`
- `utils.py`
- `validators.py`
- `logging.py`

## Rule

Core should not contain business-domain logic.

Marketplace, Trust, AI, and Platform domain rules belong in their own modules.
