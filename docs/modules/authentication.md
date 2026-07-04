# Authentication

`POST /api/v1/auth/login` accepts an email and password and returns an HS256 bearer token.
Authentication orchestration lives in `AuthenticationService`; user lookup lives in
`SqlAlchemyUserRepository`. Production deployments must provide a strong `SECRET_KEY`
and replace the seeded administrator password.
