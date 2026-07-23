# RISE Project Charter

## Project

RISE – Global AI Marketplace Platform

## Company

1stKings Ltd

## Current Status

- Current Version: v0.3.0-dev
- Current Sprint: Sprint 3 – Marketplace Core
- Current Domain: Stores

## Vision

Build RISE into a production-ready global AI marketplace and the flagship product of 1stKings Ltd.

RISE is an AI-powered global marketplace that connects buyers, sellers, professionals, and service providers through trust, location, and intelligent discovery.

## Execution Mode

From this point forward, RISE is in execution mode.

Architecture is redesigned only when necessary. Every session should produce something tangible that moves the product toward Private Alpha.

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

## Technical Stack

The technical stack for the first production version is frozen:

- Backend: Python 3.12+, FastAPI, SQLAlchemy 2.x, Alembic, PostgreSQL, Pydantic v2
- Authentication: JWT, OAuth2 Password Flow, Refresh Tokens, RBAC
- Storage: PostgreSQL, Redis, S3-compatible object storage such as AWS S3 or Cloudflare R2
- Frontend: Next.js, React, TypeScript, Tailwind CSS, TanStack Query, React Hook Form
- Mobile: React Native
- Background Jobs: Celery or Dramatiq when asynchronous processing is needed
- Search: PostgreSQL Full-Text Search initially; Elasticsearch/OpenSearch only if complexity or scale requires it
- AI: OpenAI APIs, Pinecone when semantic search or RAG becomes necessary
- DevOps: Docker, GitHub Actions, Render or Azure App Service, Nginx if self-hosting later

## Current Progress

Completed:

- Project architecture
- Repository structure
- FastAPI backend
- JWT Authentication
- User management
- 1stKings Trust MVP
- Geography: Regions, Countries, Cities
- Categories implementation
- Engineering standards
- Documentation structure

Current:

- Stores Domain

Next:

1. Products
2. Services
3. Reviews
4. Media Uploads
5. Marketplace Search

## Roadmap

| Milestone | Status |
| --- | --- |
| Platform Foundation | Complete |
| Marketplace Core | Current |
| Private Alpha | Planned |
| Commerce | Planned |
| AI Marketplace | Planned |
| Public Launch | Planned |

## Private Alpha Scope

### Buyers

- Register and log in
- Browse by region, country, and city
- Browse categories
- Search stores, products, and services
- View seller profiles
- Contact sellers

### Sellers

- Create a seller profile
- Create and manage stores
- Add products
- Add services
- Manage store information
- View basic dashboard

### Admin

- Manage users
- Manage categories
- Verify sellers
- Verify stores
- Review trust reports
- Moderate content

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

- v0.3.0 — Marketplace Foundation
- v0.4.0 — Seller Platform

Upcoming milestones:

- v0.5.0 — Private Alpha
- v0.6.0 — Commerce
- v0.7.0 — AI Marketplace
- v0.8.0 — Public Beta
- v1.0.0 — Production Launch

## Definition of Ready

Before coding any new feature:

- Requirements are clear.
- Database changes are identified.
- API contract is defined.
- Security considerations are reviewed.
- Acceptance criteria are agreed.

## Observability Direction

RISE should progressively add:

- Structured logging
- Error tracking
- `/health` and `/ready` endpoints
- Basic performance metrics
- Automated PostgreSQL backups
