import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.session import get_session
from app.stores.models import Store
from app.stores.repository import StoreRepository
from app.stores.schemas import (
    StoreCreate,
    StoreListResponse,
    StoreResponse,
    StoreUpdate,
)
from app.stores.service import StoreService
from app.users.models import User

router = APIRouter(
    prefix="/stores",
    tags=["stores"],
)

SessionDependency = Annotated[
    AsyncSession,
    Depends(get_session),
]

CurrentUserDependency = Annotated[
    User,
    Depends(get_current_user),
]


@router.get(
    "",
    response_model=StoreListResponse,
)
async def list_public_stores(
    session: SessionDependency,
    country_id: uuid.UUID | None = None,
    city_id: uuid.UUID | None = None,
    category_id: uuid.UUID | None = None,
    search: str | None = Query(default=None, max_length=150),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> StoreListResponse:
    repository = StoreRepository(session)

    stores = await repository.list_public(
        country_id=country_id,
        city_id=city_id,
        category_id=category_id,
        search=search,
        limit=limit,
        offset=offset,
    )

    total = await repository.count_public(
        country_id=country_id,
        city_id=city_id,
        category_id=category_id,
        search=search,
    )

    return StoreListResponse(
        items=[StoreResponse.model_validate(store) for store in stores],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/me",
    response_model=list[StoreResponse],
)
async def list_my_stores(
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> list[Store]:
    service = StoreService(session)
    return await service.list_owner_stores(current_user)


@router.get(
    "/slug/{slug}",
    response_model=StoreResponse,
)
async def get_store_by_slug(
    slug: str,
    session: SessionDependency,
) -> Store:
    service = StoreService(session)
    return await service.get_public_store_by_slug(slug)


@router.get(
    "/search",
    response_model=StoreListResponse,
)
async def search_stores(
    session: SessionDependency,
    q: str | None = Query(default=None, max_length=150),
    country_id: uuid.UUID | None = None,
    city_id: uuid.UUID | None = None,
    category_id: uuid.UUID | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> StoreListResponse:
    repository = StoreRepository(session)

    stores = await repository.list_public(
        country_id=country_id,
        city_id=city_id,
        category_id=category_id,
        search=q,
        limit=limit,
        offset=offset,
    )
    total = await repository.count_public(
        country_id=country_id,
        city_id=city_id,
        category_id=category_id,
        search=q,
    )

    return StoreListResponse(
        items=[StoreResponse.model_validate(store) for store in stores],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{store_id}",
    response_model=StoreResponse,
)
async def get_store(
    store_id: uuid.UUID,
    session: SessionDependency,
) -> Store:
    service = StoreService(session)
    return await service.get_public_store(store_id)


@router.post(
    "",
    response_model=StoreResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_store(
    payload: StoreCreate,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.create_store(payload, current_user)


@router.patch(
    "/{store_id}",
    response_model=StoreResponse,
)
async def update_store(
    store_id: uuid.UUID,
    payload: StoreUpdate,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.update_store(
        store_id,
        payload,
        current_user,
    )


@router.post(
    "/{store_id}/submit",
    response_model=StoreResponse,
)
async def submit_store_for_review(
    store_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.submit_for_review(
        store_id,
        current_user,
    )


@router.post(
    "/{store_id}/verify",
    response_model=StoreResponse,
)
async def verify_store(
    store_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.verify_store(
        store_id,
        current_user,
    )


@router.post(
    "/{store_id}/publish",
    response_model=StoreResponse,
)
async def publish_store(
    store_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.publish_store(
        store_id,
        current_user,
    )


@router.post(
    "/{store_id}/suspend",
    response_model=StoreResponse,
)
async def suspend_store(
    store_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.suspend_store(
        store_id,
        current_user,
    )


@router.delete(
    "/{store_id}",
    response_model=StoreResponse,
)
async def close_store(
    store_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUserDependency,
) -> Store:
    service = StoreService(session)
    return await service.close_store(
        store_id,
        current_user,
    )
