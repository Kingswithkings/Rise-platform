from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.repositories import UserReader
from app.auth.security import create_access_token, hash_password, verify_password
from app.trust.service import create_trust_profile
from app.users.models import User


class InvalidCredentialsError(Exception):
    pass


class EmailAlreadyRegisteredError(Exception):
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


class RegistrationService:
    def __init__(self, session: AsyncSession, users: UserReader) -> None:
        self._session = session
        self._users = users

    async def register(self, email: str, password: str) -> User:
        normalized_email = email.lower()
        if await self._users.get_by_email(normalized_email):
            raise EmailAlreadyRegisteredError

        user = User(email=normalized_email, hashed_password=hash_password(password))
        self._session.add(user)
        await self._session.flush()
        await create_trust_profile(self._session, user.id)
        await self._session.commit()
        await self._session.refresh(user)
        return user
