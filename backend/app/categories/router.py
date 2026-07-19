from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.categories import service
from app.categories.schemas import (
    CategoryCreate,
    CategoryResponse,
    CategoryTreeResponse,
    CategoryUpdate,
)
from app.database.session import get_session
from app.users.models import User

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)
SessionDependency = Annotated[AsyncSession, Depends(get_session)]
CurrentUserDependency = Annotated[User, Depends(get_current_user)]


def require_admin(
    current_user: CurrentUserDependency,
) -> User:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    payload: CategoryCreate,
    db: SessionDependency,
    _: Annotated[User, Depends(require_admin)],
):
    return await service.create_category(db, payload)


@router.get("", response_model=list[CategoryResponse])
async def list_categories(
    db: SessionDependency,
    include_inactive: bool = Query(default=False),
):
    return await service.list_categories(
        db,
        include_inactive=include_inactive,
    )


@router.get("/tree", response_model=list[CategoryTreeResponse])
async def get_category_tree(db: SessionDependency):
    return await service.build_category_tree(db)


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: UUID,
    db: SessionDependency,
):
    return await service.get_category(db, category_id)


@router.patch("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: UUID,
    payload: CategoryUpdate,
    db: SessionDependency,
    _: Annotated[User, Depends(require_admin)],
):
    return await service.update_category(db, category_id, payload)


@router.delete("/{category_id}", response_model=CategoryResponse)
async def deactivate_category(
    category_id: UUID,
    db: SessionDependency,
    _: Annotated[User, Depends(require_admin)],
):
    return await service.deactivate_category(db, category_id)
