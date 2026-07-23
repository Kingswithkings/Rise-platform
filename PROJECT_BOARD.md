# RISE Project Board

## Current Sprint

Sprint 3 – Marketplace Core

## Current Domain

🏪 Stores — Next

## Current Phase

Phase 2 – Marketplace Core

## Delivery Mode

Execution Mode

## Overall Progress

- [x] Foundation
- [x] Authentication
- [x] Users
- [x] 1stKings Trust
- [x] Geography
- [x] Categories
- [ ] Stores
- [ ] Products
- [ ] Services
- [ ] Media Management
- [ ] Reviews & Ratings
- [ ] Marketplace Search
- [ ] Favorites
- [ ] Messaging
- [ ] Notifications
- [ ] Orders
- [ ] Payments
- [ ] Delivery
- [ ] Seller Dashboard
- [ ] Analytics
- [ ] AI

## Sprint 3 Backlog

| Priority | Domain | Status |
| --- | --- | --- |
| 1 | Categories | Testing |
| 2 | Stores | Next |
| 3 | Products | Planned |
| 4 | Services | Planned |
| 5 | Marketplace Search | Planned |

## Sprint 3 Task Board

| Task | Status |
| --- | --- |
| Authentication | Complete |
| Users | Complete |
| Geography | Complete |
| 1stKings Trust | Complete |
| Categories | Testing |
| Stores | Next |
| Products | Planned |
| Services | Planned |
| Reviews | Planned |
| Media Uploads | Planned |
| Marketplace Search | Planned |

## Next Milestone

RISE v0.5.0 – Private Alpha

## Immediate Implementation Sequence

1. Complete Categories, including automated tests.
2. Build Stores.
3. Build Products.
4. Build Services.
5. Implement Marketplace Search.

## Session Exit Criteria

Every build session should end with:

- [ ] New working code
- [ ] Passing tests
- [ ] Updated documentation
- [ ] Commit ready to merge

## Stores Completion Checklist

- [x] SQLAlchemy models
- [ ] Alembic migration
- [x] Pydantic schemas
- [x] Repository
- [x] Service
- [x] Router
- [x] Authentication
- [x] Seller authorization
- [x] Store validation
- [ ] Swagger tests
- [x] Unit tests
- [x] README
- [x] Sprint documentation
- [ ] Git commit

## Private Alpha Scope

- [x] Register and log in
- [ ] Create a seller profile
- [ ] Create a verified store
- [ ] Add products
- [ ] Add services
- [ ] Manage store information
- [x] Browse categories
- [ ] Search the marketplace
- [ ] View seller profiles
- [x] View trust badges
- [ ] Contact sellers

## Engineering Backlog

| Epic | Scope | Status |
| --- | --- | --- |
| Epic 1 – Identity | Authentication, Users, Roles | Complete |
| Epic 2 – Geography | Regions, Countries, Cities | Complete |
| Epic 3 – Trust | Trust Profiles, Verification, Trust Events | Complete |
| Epic 4 – Marketplace | Categories, Stores, Products, Services | In Progress |
| Epic 5 – Discovery | Search, Filters, Nearby Results | Planned |
| Epic 6 – Engagement | Reviews, Favorites, Messaging, Notifications | Planned |
| Epic 7 – Commerce | Orders, Payments, Shipping | Planned |
| Epic 8 – Intelligence | AI Assistant, Recommendations, Fraud Detection | Planned |

## Private Alpha End-to-End Goal

1. User registers.
2. User creates a seller profile.
3. Seller creates a store.
4. Seller uploads products and services.
5. Buyers browse by region and category.
6. Buyers search for stores, products, or services.
7. Buyers see Trust badges and seller information.
8. Buyers contact sellers.

## Definition of Done

A domain is complete only when:

- [ ] Business rules documented
- [ ] README completed
- [ ] Models completed
- [ ] Schemas completed
- [ ] Repository completed
- [ ] Service completed
- [ ] Router completed
- [ ] Alembic migration completed
- [ ] Tests passing
- [ ] Swagger verified
- [ ] Sprint documentation updated
- [ ] Release notes updated

## Git Workflow

```text
main
└── develop
    ├── feature/categories
    ├── feature/stores
    ├── feature/products
    ├── feature/services
    └── feature/search
```

Every feature is built in its own branch and merged into `develop` after review.

## Deployment Environments

```text
Local Development
↓
Staging
↓
Production
```
