import uuid

import pytest

from app.auth.security import hash_password
from app.auth.services import AuthenticationService, InvalidCredentialsError
from app.users.models import User


class FakeUserRepository:
    def __init__(self, user: User | None) -> None:
        self.user = user

    async def get_by_email(self, email: str) -> User | None:
        return self.user if self.user and self.user.email == email else None


@pytest.mark.asyncio
async def test_authenticate_returns_token_for_valid_credentials() -> None:
    user = User(
        id=uuid.uuid4(),
        email="person@example.com",
        hashed_password=hash_password("StrongPassword1!"),
        is_active=True,
    )
    token = await AuthenticationService(FakeUserRepository(user)).authenticate(
        "person@example.com", "StrongPassword1!"
    )
    assert token


@pytest.mark.asyncio
async def test_authenticate_rejects_invalid_credentials() -> None:
    with pytest.raises(InvalidCredentialsError):
        await AuthenticationService(FakeUserRepository(None)).authenticate(
            "missing@example.com", "wrong"
        )
