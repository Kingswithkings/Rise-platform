import uuid

from sqlalchemy import Select, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.categories.models import Category
from app.geography.models import City, Country
from app.stores.models import Store, StoreStatus


class StoreRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, store: Store) -> Store:
        self.session.add(store)
        await self.session.flush()
        await self.session.refresh(store)
        return store

    async def get_by_id(self, store_id: uuid.UUID) -> Store | None:
        result = await self.session.execute(
            select(Store).where(Store.id == store_id)
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str) -> Store | None:
        result = await self.session.execute(
            select(Store).where(Store.slug == slug)
        )
        return result.scalar_one_or_none()

    async def list_public(
        self,
        *,
        country_id: uuid.UUID | None = None,
        city_id: uuid.UUID | None = None,
        category_id: uuid.UUID | None = None,
        search: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Store]:
        statement: Select[tuple[Store]] = select(Store).where(
            Store.status == StoreStatus.PUBLISHED,
            Store.active.is_(True),
            Store.verified.is_(True),
        )

        if country_id is not None:
            statement = statement.where(Store.country_id == country_id)

        if city_id is not None:
            statement = statement.where(Store.city_id == city_id)

        if category_id is not None:
            statement = statement.where(Store.category_id == category_id)

        if search:
            search_term = f"%{search.strip()}%"
            statement = statement.where(
                or_(
                    Store.store_name.ilike(search_term),
                    Store.description.ilike(search_term),
                    Store.address.ilike(search_term),
                )
            )

        statement = (
            statement
            .order_by(
                Store.trust_score.desc(),
                Store.average_rating.desc(),
                Store.created_at.desc(),
            )
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def count_public(
        self,
        *,
        country_id: uuid.UUID | None = None,
        city_id: uuid.UUID | None = None,
        category_id: uuid.UUID | None = None,
        search: str | None = None,
    ) -> int:
        statement = select(func.count(Store.id)).where(
            Store.status == StoreStatus.PUBLISHED,
            Store.active.is_(True),
            Store.verified.is_(True),
        )

        if country_id is not None:
            statement = statement.where(Store.country_id == country_id)

        if city_id is not None:
            statement = statement.where(Store.city_id == city_id)

        if category_id is not None:
            statement = statement.where(Store.category_id == category_id)

        if search:
            search_term = f"%{search.strip()}%"
            statement = statement.where(
                or_(
                    Store.store_name.ilike(search_term),
                    Store.description.ilike(search_term),
                    Store.address.ilike(search_term),
                )
            )

        result = await self.session.execute(statement)
        return int(result.scalar_one())

    async def list_by_owner(
        self,
        owner_id: uuid.UUID,
    ) -> list[Store]:
        result = await self.session.execute(
            select(Store)
            .where(Store.owner_id == owner_id)
            .order_by(Store.created_at.desc())
        )
        return list(result.scalars().all())

    async def save(self, store: Store) -> Store:
        await self.session.flush()
        await self.session.refresh(store)
        return store

    async def delete(self, store: Store) -> None:
        await self.session.delete(store)
        await self.session.flush()

    async def get_category(self, category_id: uuid.UUID) -> Category | None:
        result = await self.session.execute(
            select(Category).where(Category.id == category_id)
        )
        return result.scalar_one_or_none()

    async def get_country(self, country_id: uuid.UUID) -> Country | None:
        result = await self.session.execute(
            select(Country).where(Country.id == country_id)
        )
        return result.scalar_one_or_none()

    async def get_city(self, city_id: uuid.UUID) -> City | None:
        result = await self.session.execute(
            select(City).where(City.id == city_id)
        )
        return result.scalar_one_or_none()
