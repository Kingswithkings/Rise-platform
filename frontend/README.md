# Frontend

## Purpose

The frontend provides the customer and operator web experiences using Next.js and
TypeScript.

## Architecture

- `app/` — routes and page composition
- `features/` — feature-owned UI and behavior
- `components/` — shared presentation
- `services/` — API clients
- `providers/`, `hooks/`, `store/`, and `types/` — shared application infrastructure

## Run locally

```bash
docker compose up --build frontend
```

Open `http://localhost:3000`.

## Coding standards

Strict TypeScript, ESLint, Prettier, Vitest, and Playwright are required. Tailwind and
shadcn/ui remain planned Sprint 1 work and must be integrated through a reviewed task.
