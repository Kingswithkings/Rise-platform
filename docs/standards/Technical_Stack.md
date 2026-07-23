# Technical Stack

Technology choices are frozen for the first production version unless there is a strong architectural reason to change them.

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
- Redis for caching and background tasks when needed
- S3-compatible object storage, such as AWS S3 or Cloudflare R2, for images

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

- React Native after the web platform reaches stability

## AI

- OpenAI APIs
- Pinecone when semantic search or RAG becomes necessary

## DevOps

- Docker
- GitHub Actions
- Render or Azure App Service for initial deployment
- Nginx if self-hosting later
