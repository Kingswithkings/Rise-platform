# Git Workflow

```text
main
└── develop
    ├── feature/categories
    ├── feature/stores
    ├── feature/products
    ├── feature/services
    └── feature/search
```

## Rules

Every feature branch should include:

- A focused set of changes.
- Passing tests.
- Documentation updates.

Feature branches merge into `develop` after review.

`main` represents production-ready code.
