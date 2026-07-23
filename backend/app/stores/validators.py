import uuid

from fastapi import HTTPException, status

from app.stores.models import Store, StoreStatus
from app.stores.repository import StoreRepository
from app.users.models import User


def validate_seller(user: User) -> None:
    if not (getattr(user, "is_seller", False) or user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Seller access required",
        )


def validate_admin(user: User) -> None:
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required",
        )


async def validate_slug(
    repository: StoreRepository,
    slug: str,
    *,
    current_store_id: uuid.UUID | None = None,
) -> str:
    normalized_slug = slug.strip().lower()
    existing_store = await repository.get_by_slug(normalized_slug)

    if existing_store is not None and existing_store.id != current_store_id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A store with this slug already exists",
        )

    return normalized_slug


async def validate_category(
    repository: StoreRepository,
    category_id: uuid.UUID,
) -> None:
    category = await repository.get_category(category_id)

    if category is None or not category.active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )


async def validate_country(
    repository: StoreRepository,
    country_id: uuid.UUID,
) -> None:
    country = await repository.get_country(country_id)

    if country is None or not country.active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Country not found",
        )


async def validate_city(
    repository: StoreRepository,
    *,
    city_id: uuid.UUID,
    country_id: uuid.UUID,
) -> None:
    city = await repository.get_city(city_id)

    if city is None or not city.active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found",
        )

    if city.country_id != country_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="City does not belong to the selected country",
        )


def validate_store_owner(store: Store, user: User) -> None:
    if store.owner_id != user.id and not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only manage your own stores",
        )


def validate_store_is_public(store: Store) -> None:
    if (
        store.status != StoreStatus.PUBLISHED
        or not store.verified
        or not store.active
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Store not found",
        )


def validate_store_status_for_publish(store: Store) -> None:
    if not store.verified:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Store must be verified before publication",
        )

    if store.status != StoreStatus.VERIFIED:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Only verified stores can be published",
        )


def validate_submission_readiness(store: Store) -> None:
    missing_fields: list[str] = []

    required_values = {
        "store_name": store.store_name,
        "description": store.description,
        "email": store.email,
        "address": store.address,
        "category_id": store.category_id,
        "country_id": store.country_id,
        "city_id": store.city_id,
    }

    for field_name, value in required_values.items():
        if value is None or (isinstance(value, str) and not value.strip()):
            missing_fields.append(field_name)

    if missing_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "message": "Store profile is incomplete",
                "missing_fields": missing_fields,
            },
        )


async def validate_location_and_category(
    repository: StoreRepository,
    *,
    category_id: uuid.UUID,
    country_id: uuid.UUID,
    city_id: uuid.UUID,
) -> None:
    await validate_category(repository, category_id)
    await validate_country(repository, country_id)
    await validate_city(
        repository,
        city_id=city_id,
        country_id=country_id,
    )
