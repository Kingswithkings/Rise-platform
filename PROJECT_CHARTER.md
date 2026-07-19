# RISE Project Charter

## Project

RISE – Global AI Marketplace Platform

## Company

1stkings INTERNATIONAL

## Current Status

- Current Version: v0.3.0-dev
- Current Sprint: Sprint 3 – Marketplace Foundation
- Current Domain: Categories

## Vision

Build RISE into a production-ready global AI marketplace and the flagship product of 1stkings INTERNATIONAL.

## Scope

RISE combines marketplace, trust, AI, and reusable platform capabilities.

### Marketplace

- Regions
- Countries
- Cities
- Categories
- Stores
- Products
- Services
- Marketplace Search
- Orders
- Payments

### Trust

- 1stKings Trust profiles
- Verification
- Reviews
- Risk
- Fraud
- Badges

### AI

- AI Search
- Recommendations
- Seller Assistant
- Buyer Assistant
- Business Insights

### Platform

- Identity
- Payments
- Notifications
- Analytics
- Search
- Maps
- Files

## Architecture

RISE uses a modular monolith architecture organized by business domain.

Principles:

- Business domains first.
- API-first design.
- Modular monolith until service extraction is justified.
- Security by design.
- Observability by default.
- Automated testing for business logic.
- Documentation is part of delivery.

## Current Progress

Completed:

- Project architecture
- Repository structure
- FastAPI backend
- JWT Authentication
- User management
- 1stKings Trust MVP
- Geography: Regions, Countries, Cities

Current:

- Categories Domain

Next:

1. Stores
2. Products
3. Services
4. Marketplace Search

## Roadmap

| Milestone | Status |
| --- | --- |
| Platform Foundation | Complete |
| Marketplace Foundation | In Progress |
| Private Alpha | Planned |
| Commerce | Planned |
| AI Marketplace | Planned |
| Public Launch | Planned |

## Engineering Pack Standard

Every new domain is delivered as an Engineering Pack.

Each pack includes:

- Business documentation
- Domain overview
- User stories
- Business rules
- Acceptance criteria
- Architecture
- Database design
- API design
- Models
- Schemas
- Repository
- Service
- Router
- Permissions
- Validation
- Unit tests
- Integration tests where useful
- Test data
- Swagger validation
- README
- Sprint update
- Release notes
- ADR when needed

## Definition of Done

A domain is complete only when:

- Business rules are documented.
- README is completed.
- Models are completed.
- Schemas are completed.
- Repository is completed.
- Service is completed.
- Router is completed.
- Alembic migration is completed.
- Tests are passing.
- Swagger is verified.
- Sprint documentation is updated.
- Release notes are updated.

## Pull Request Review Questions

Every Pull Request must answer:

- What problem does this solve?
- What changed?
- Does it change the database?
- Does it add or modify APIs?
- Are tests included?
- Is documentation updated?

If any answer is missing, the work is not ready for review.

## Release Strategy

Current target:

- v0.4.0 — complete Marketplace Foundation

Upcoming milestones:

- v0.5.0 — Private Alpha
- v0.6.0 — Commerce
- v0.7.0 — Buyer Platform
- v0.8.0 — AI Marketplace
- v0.9.0 — Beta
- v1.0.0 — Public Launch
