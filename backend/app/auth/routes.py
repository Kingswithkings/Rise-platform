from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.repositories import SqlAlchemyUserRepository
from app.auth.schemas import LoginRequest, RegistrationRequest, TokenResponse, UserResponse
from app.auth.services import (
    AuthenticationService,
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    RegistrationService,
)
from app.database.session import get_session

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    registration: RegistrationRequest,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> UserResponse:
    users = SqlAlchemyUserRepository(session)
    try:
        user = await RegistrationService(session, users).register(
            registration.email, registration.password
        )
    except EmailAlreadyRegisteredError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        ) from error
    return UserResponse.model_validate(user)


@router.post("/login", response_model=TokenResponse)
async def login(
    credentials: LoginRequest,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> TokenResponse:
    service = AuthenticationService(SqlAlchemyUserRepository(session))
    try:
        token = await service.authenticate(credentials.email, credentials.password)
    except InvalidCredentialsError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        ) from error
    return TokenResponse(access_token=token)
