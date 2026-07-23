# Technical Stack Final

## Status

Accepted for first production version.

## Backend

- Python 3.12+
- FastAPI
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- Pydantic v2

## Authentication

- JWT
- OAuth2 Password Flow
- Refresh Tokens
- Role-Based Access Control

## Storage

- PostgreSQL
- Redis
- S3-compatible object storage

## Background Jobs

- Celery or Dramatiq when asynchronous processing is needed

## Search

- PostgreSQL Full-Text Search initially
- Elasticsearch/OpenSearch only if search complexity or scale requires it

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- TanStack Query
- React Hook Form

## Mobile

- React Native

## AI

- OpenAI APIs
- Pinecone when semantic search or RAG becomes necessary

## DevOps

- Docker
- GitHub Actions
- Render or Azure App Service
- Nginx if self-hosting later
