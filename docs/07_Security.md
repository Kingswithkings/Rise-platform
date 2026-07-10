# Security

## Baseline controls

- JWT bearer authentication
- Argon2 password hashing
- Secrets supplied through environment variables
- Input validation through typed schemas
- Least-privilege database and deployment credentials
- Dependency and code checks in CI

Production must use a strong `SECRET_KEY` and replace all development seed credentials.
Secrets must never be committed.
