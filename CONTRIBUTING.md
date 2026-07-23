# Contributing to RISE

## Branching

```text
main
└── develop
    ├── feature/categories
    ├── feature/stores
    ├── feature/products
    ├── feature/services
    └── feature/search
```

Feature branches merge into `develop` after review.

`main` is reserved for production-ready code.

## Pull Request Checklist

Every Pull Request must answer:

- What problem does this solve?
- What changed?
- Does it change the database?
- Does it add or modify APIs?
- Are tests included?
- Is documentation updated?

## Definition of Ready

Before coding:

- Requirements are clear.
- Database changes are identified.
- API contract is defined.
- Security considerations are reviewed.
- Acceptance criteria are agreed.

## Definition of Done

A feature is complete only when:

- Code is implemented.
- Database migration exists.
- Tests pass.
- Swagger documentation is verified.
- README is updated.
- Sprint notes are updated.
- Code is reviewed.
- Work is merged into `develop`.
