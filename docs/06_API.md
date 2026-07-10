# API

FastAPI exposes the versioned API under `/api/v1`. OpenAPI is the authoritative
machine-readable contract.

## Local endpoints

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- OpenAPI: `http://localhost:8000/openapi.json`
- Health: `http://localhost:8000/health`

Routes must use typed request and response schemas and return consistent HTTP status
codes.
