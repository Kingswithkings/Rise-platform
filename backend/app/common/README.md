# Common Module

## Purpose

The Common module contains reusable domain-support components that are not tied to one business domain.

## Planned Responsibilities

- Base SQLAlchemy model
- Base repository
- Base service
- Validators
- Slug generation
- File upload utilities

## Rule

Common code must be reusable by multiple domains.

If logic belongs only to Categories, Stores, Products, Services, Trust, or another specific domain, keep it inside that domain.
