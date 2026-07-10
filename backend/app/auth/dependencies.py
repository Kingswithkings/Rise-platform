import uuid
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.repositories import SqlAlchemyUserRepository
from app.config.settings import settings
from app.database.session import get_session
from app.users.models import User

bearer_scheme = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> User:
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired access token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(credentials.credentials, settings.secret_key, algorithms=["HS256"])
        subject = payload.get("sub")
        user_id = uuid.UUID(subject) if isinstance(subject, str) else None
        if user_id is None:
            raise unauthorized
    except (jwt.PyJWTError, ValueError) as error:
        raise unauthorized from error

    user = await SqlAlchemyUserRepository(session).get_by_id(user_id)
    if user is None or not user.is_active:
        raise unauthorized
    return user
