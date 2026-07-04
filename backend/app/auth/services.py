from app.auth.repositories import UserReader
from app.auth.security import create_access_token, verify_password


class InvalidCredentialsError(Exception):
    pass


class AuthenticationService:
    def __init__(self, users: UserReader) -> None:
        self._users = users

    async def authenticate(self, email: str, password: str) -> str:
        user = await self._users.get_by_email(email.lower())
        credentials_invalid = user is None or not (
            user.is_active and verify_password(password, user.hashed_password)
        )
        if credentials_invalid:
            raise InvalidCredentialsError
        return create_access_token(str(user.id))
