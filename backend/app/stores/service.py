import uuid

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.stores.models import Store, StoreStatus
from app.stores.repository import StoreRepository
from app.stores.schemas import StoreCreate, StoreUpdate
from app.stores.validators import (
    validate_admin,
    validate_location_and_category,
    validate_seller,
    validate_slug,
    validate_store_is_public,
    validate_store_owner,
    validate_store_status_for_publish,
    validate_submission_readiness,
)
from app.users.models import User


class StoreService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.repository = StoreRepository(session)

    async def create_store(
        self,
        payload: StoreCreate,
        current_user: User,
    ) -> Store:
        validate_seller(current_user)

        slug = await validate_slug(self.repository, payload.slug)
        await validate_location_and_category(
            self.repository,
            category_id=payload.category_id,
            country_id=payload.country_id,
            city_id=payload.city_id,
        )

        store = Store(
            owner_id=current_user.id,
            category_id=payload.category_id,
            country_id=payload.country_id,
            city_id=payload.city_id,
            store_name=payload.store_name.strip(),
            slug=slug,
            description=payload.description,
            logo_url=str(payload.logo_url) if payload.logo_url else None,
            cover_url=str(payload.cover_url) if payload.cover_url else None,
            email=str(payload.email),
            phone=payload.phone,
            website=str(payload.website) if payload.website else None,
            address=payload.address.strip(),
            postal_code=payload.postal_code,
            latitude=payload.latitude,
            longitude=payload.longitude,
            status=StoreStatus.DRAFT,
            verified=False,
            active=True,
            trust_score=50,
        )

        return await self._create_and_commit(store)

    async def get_public_store(
        self,
        store_id: uuid.UUID,
    ) -> Store:
        store = await self._get_store_or_404(store_id)
        validate_store_is_public(store)
        return store

    async def get_public_store_by_slug(
        self,
        slug: str,
    ) -> Store:
        store = await self.repository.get_by_slug(slug.strip().lower())

        if store is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Store not found",
            )

        validate_store_is_public(store)
        return store

    async def list_owner_stores(
        self,
        current_user: User,
    ) -> list[Store]:
        return await self.repository.list_by_owner(current_user.id)

    async def update_store(
        self,
        store_id: uuid.UUID,
        payload: StoreUpdate,
        current_user: User,
    ) -> Store:
        store = await self._get_store_or_404(store_id)
        validate_store_owner(store, current_user)

        updates = payload.model_dump(exclude_unset=True)

        if "slug" in updates and updates["slug"] is not None:
            updates["slug"] = await validate_slug(
                self.repository,
                updates["slug"],
                current_store_id=store.id,
            )

        category_id = updates.get("category_id", store.category_id)
        country_id = updates.get("country_id", store.country_id)
        city_id = updates.get("city_id", store.city_id)

        if any(key in updates for key in ("category_id", "country_id", "city_id")):
            await validate_location_and_category(
                self.repository,
                category_id=category_id,
                country_id=country_id,
                city_id=city_id,
            )

        for url_field in ("logo_url", "cover_url", "website"):
            if url_field in updates and updates[url_field] is not None:
                updates[url_field] = str(updates[url_field])

        if "email" in updates and updates["email"] is not None:
            updates["email"] = str(updates["email"])

        if "store_name" in updates and updates["store_name"] is not None:
            updates["store_name"] = updates["store_name"].strip()

        if "address" in updates and updates["address"] is not None:
            updates["address"] = updates["address"].strip()

        for field_name, value in updates.items():
            setattr(store, field_name, value)

        return await self._save_and_commit(store)

    async def submit_for_review(
        self,
        store_id: uuid.UUID,
        current_user: User,
    ) -> Store:
        store = await self._get_store_or_404(store_id)
        validate_store_owner(store, current_user)

        if store.status not in {StoreStatus.DRAFT, StoreStatus.SUSPENDED}:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only draft or suspended stores can be submitted for review",
            )

        validate_submission_readiness(store)

        store.status = StoreStatus.PENDING_REVIEW
        store.verified = False

        return await self._save_and_commit(store)

    async def verify_store(
        self,
        store_id: uuid.UUID,
        current_user: User,
    ) -> Store:
        validate_admin(current_user)

        store = await self._get_store_or_404(store_id)

        if store.status != StoreStatus.PENDING_REVIEW:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Store must be pending review before verification",
            )

        store.verified = True
        store.status = StoreStatus.VERIFIED

        return await self._save_and_commit(store)

    async def publish_store(
        self,
        store_id: uuid.UUID,
        current_user: User,
    ) -> Store:
        validate_admin(current_user)

        store = await self._get_store_or_404(store_id)
        validate_store_status_for_publish(store)

        store.status = StoreStatus.PUBLISHED
        store.active = True

        return await self._save_and_commit(store)

    async def suspend_store(
        self,
        store_id: uuid.UUID,
        current_user: User,
    ) -> Store:
        validate_admin(current_user)

        store = await self._get_store_or_404(store_id)
        store.status = StoreStatus.SUSPENDED
        store.active = False

        return await self._save_and_commit(store)

    async def close_store(
        self,
        store_id: uuid.UUID,
        current_user: User,
    ) -> Store:
        store = await self._get_store_or_404(store_id)
        validate_store_owner(store, current_user)

        store.status = StoreStatus.SUSPENDED
        store.active = False

        return await self._save_and_commit(store)

    async def _get_store_or_404(
        self,
        store_id: uuid.UUID,
    ) -> Store:
        store = await self.repository.get_by_id(store_id)

        if store is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Store not found",
            )

        return store

    async def _create_and_commit(self, store: Store) -> Store:
        try:
            created_store = await self.repository.create(store)
            await self.session.commit()
            await self.session.refresh(created_store)
            return created_store
        except Exception:
            await self.session.rollback()
            raise

    async def _save_and_commit(self, store: Store) -> Store:
        try:
            saved_store = await self.repository.save(store)
            await self.session.commit()
            await self.session.refresh(saved_store)
            return saved_store
        except Exception:
            await self.session.rollback()
            raise
