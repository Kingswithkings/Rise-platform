import uuid
from types import SimpleNamespace

import pytest
from fastapi import HTTPException, status

from app.stores.models import Store, StoreStatus
from app.stores.repository import StoreRepository
from app.stores.schemas import StoreCreate, StoreUpdate
from app.stores.service import StoreService


class FakeSession:
    async def commit(self) -> None:
        return None

    async def rollback(self) -> None:
        return None

    async def refresh(self, _instance) -> None:
        return None


def seller_user(user_id: uuid.UUID | None = None):
    return SimpleNamespace(
        id=user_id or uuid.uuid4(),
        is_active=True,
        is_admin=False,
        is_seller=True,
    )


def non_seller_user(user_id: uuid.UUID | None = None):
    return SimpleNamespace(
        id=user_id or uuid.uuid4(),
        is_active=True,
        is_admin=False,
        is_seller=False,
    )


def admin_user(user_id: uuid.UUID | None = None):
    return SimpleNamespace(
        id=user_id or uuid.uuid4(),
        is_active=True,
        is_admin=True,
        is_seller=True,
    )


def store_payload(
    *,
    category_id: uuid.UUID | None = None,
    country_id: uuid.UUID | None = None,
    city_id: uuid.UUID | None = None,
) -> StoreCreate:
    return StoreCreate(
        category_id=category_id or uuid.uuid4(),
        country_id=country_id or uuid.uuid4(),
        city_id=city_id or uuid.uuid4(),
        store_name="Kings Electronics",
        slug="kings-electronics",
        description="Electronic products and accessories",
        email="seller@example.com",
        address="1 Market Street",
    )


def active_entity(**kwargs):
    return SimpleNamespace(active=True, **kwargs)


def make_store(
    *,
    owner_id: uuid.UUID | None = None,
    status: StoreStatus = StoreStatus.DRAFT,
    verified: bool = False,
    active: bool = True,
) -> Store:
    return Store(
        id=uuid.uuid4(),
        owner_id=owner_id or uuid.uuid4(),
        category_id=uuid.uuid4(),
        country_id=uuid.uuid4(),
        city_id=uuid.uuid4(),
        store_name="Old Store",
        slug="old-store",
        description="Existing store",
        email="seller@example.com",
        address="1 Market Street",
        status=status,
        verified=verified,
        active=active,
        trust_score=50,
    )


def patch_valid_location(monkeypatch, payload: StoreCreate) -> None:
    async def get_category(self, category_id):
        return active_entity(id=category_id)

    async def get_country(self, country_id):
        return active_entity(id=country_id)

    async def get_city(self, city_id):
        return active_entity(id=city_id, country_id=payload.country_id)

    monkeypatch.setattr(StoreRepository, "get_category", get_category)
    monkeypatch.setattr(StoreRepository, "get_country", get_country)
    monkeypatch.setattr(StoreRepository, "get_city", get_city)


@pytest.mark.asyncio
async def test_create_store_sets_draft_status_and_baseline_trust_score(monkeypatch) -> None:
    payload = store_payload()
    user = seller_user()

    async def no_existing_slug(self, slug):
        return None

    async def create(self, store):
        return store

    monkeypatch.setattr(StoreRepository, "get_by_slug", no_existing_slug)
    monkeypatch.setattr(StoreRepository, "create", create)
    patch_valid_location(monkeypatch, payload)

    result = await StoreService(FakeSession()).create_store(payload, user)

    assert result.owner_id == user.id
    assert result.store_name == "Kings Electronics"
    assert result.status == StoreStatus.DRAFT
    assert result.verified is False
    assert result.active is True
    assert result.trust_score == 50


@pytest.mark.asyncio
async def test_create_store_requires_seller_access() -> None:
    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(
            store_payload(),
            non_seller_user(),
        )

    assert error.value.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_create_store_rejects_duplicate_slug(monkeypatch) -> None:
    payload = store_payload()

    async def existing_slug(self, slug):
        return make_store()

    monkeypatch.setattr(StoreRepository, "get_by_slug", existing_slug)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(payload, seller_user())

    assert error.value.status_code == status.HTTP_409_CONFLICT


@pytest.mark.asyncio
async def test_create_store_rejects_invalid_category(monkeypatch) -> None:
    payload = store_payload()

    async def no_existing_slug(self, slug):
        return None

    async def missing_category(self, category_id):
        return None

    monkeypatch.setattr(StoreRepository, "get_by_slug", no_existing_slug)
    monkeypatch.setattr(StoreRepository, "get_category", missing_category)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(payload, seller_user())

    assert error.value.status_code == status.HTTP_404_NOT_FOUND
    assert error.value.detail == "Category not found"


@pytest.mark.asyncio
async def test_create_store_rejects_invalid_country(monkeypatch) -> None:
    payload = store_payload()

    async def no_existing_slug(self, slug):
        return None

    async def get_category(self, category_id):
        return active_entity(id=category_id)

    async def missing_country(self, country_id):
        return None

    monkeypatch.setattr(StoreRepository, "get_by_slug", no_existing_slug)
    monkeypatch.setattr(StoreRepository, "get_category", get_category)
    monkeypatch.setattr(StoreRepository, "get_country", missing_country)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(payload, seller_user())

    assert error.value.status_code == status.HTTP_404_NOT_FOUND
    assert error.value.detail == "Country not found"


@pytest.mark.asyncio
async def test_create_store_rejects_invalid_city(monkeypatch) -> None:
    payload = store_payload()

    async def no_existing_slug(self, slug):
        return None

    async def get_category(self, category_id):
        return active_entity(id=category_id)

    async def get_country(self, country_id):
        return active_entity(id=country_id)

    async def missing_city(self, city_id):
        return None

    monkeypatch.setattr(StoreRepository, "get_by_slug", no_existing_slug)
    monkeypatch.setattr(StoreRepository, "get_category", get_category)
    monkeypatch.setattr(StoreRepository, "get_country", get_country)
    monkeypatch.setattr(StoreRepository, "get_city", missing_city)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(payload, seller_user())

    assert error.value.status_code == status.HTTP_404_NOT_FOUND
    assert error.value.detail == "City not found"


@pytest.mark.asyncio
async def test_create_store_rejects_city_from_different_country(monkeypatch) -> None:
    payload = store_payload()

    async def no_existing_slug(self, slug):
        return None

    async def get_category(self, category_id):
        return active_entity(id=category_id)

    async def get_country(self, country_id):
        return active_entity(id=country_id)

    async def get_city(self, city_id):
        return active_entity(id=city_id, country_id=uuid.uuid4())

    monkeypatch.setattr(StoreRepository, "get_by_slug", no_existing_slug)
    monkeypatch.setattr(StoreRepository, "get_category", get_category)
    monkeypatch.setattr(StoreRepository, "get_country", get_country)
    monkeypatch.setattr(StoreRepository, "get_city", get_city)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).create_store(payload, seller_user())

    assert error.value.status_code == status.HTTP_400_BAD_REQUEST
    assert error.value.detail == "City does not belong to the selected country"


@pytest.mark.asyncio
async def test_owner_can_update_store(monkeypatch) -> None:
    owner = seller_user()
    store = make_store(owner_id=owner.id)

    async def get_by_id(self, store_id):
        return store

    async def save(self, current_store):
        return current_store

    monkeypatch.setattr(StoreRepository, "get_by_id", get_by_id)
    monkeypatch.setattr(StoreRepository, "save", save)

    result = await StoreService(FakeSession()).update_store(
        store.id,
        StoreUpdate(store_name="Updated Store"),
        owner,
    )

    assert result.store_name == "Updated Store"


@pytest.mark.asyncio
async def test_non_owner_update_is_denied(monkeypatch) -> None:
    store = make_store()

    async def get_by_id(self, store_id):
        return store

    monkeypatch.setattr(StoreRepository, "get_by_id", get_by_id)

    with pytest.raises(HTTPException) as error:
        await StoreService(FakeSession()).update_store(
            store.id,
            StoreUpdate(store_name="Updated Store"),
            seller_user(),
        )

    assert error.value.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_admin_can_verify_store(monkeypatch) -> None:
    store = make_store(status=StoreStatus.PENDING_REVIEW, verified=False)

    async def get_by_id(self, store_id):
        return store

    async def save(self, current_store):
        return current_store

    monkeypatch.setattr(StoreRepository, "get_by_id", get_by_id)
    monkeypatch.setattr(StoreRepository, "save", save)

    result = await StoreService(FakeSession()).verify_store(store.id, admin_user())

    assert result.verified is True
    assert result.status == StoreStatus.VERIFIED


@pytest.mark.asyncio
async def test_admin_can_publish_verified_store(monkeypatch) -> None:
    store = make_store(
        status=StoreStatus.VERIFIED,
        verified=True,
        active=True,
    )

    async def get_by_id(self, store_id):
        return store

    async def save(self, current_store):
        return current_store

    monkeypatch.setattr(StoreRepository, "get_by_id", get_by_id)
    monkeypatch.setattr(StoreRepository, "save", save)

    result = await StoreService(FakeSession()).publish_store(store.id, admin_user())

    assert result.status == StoreStatus.PUBLISHED
    assert result.active is True
