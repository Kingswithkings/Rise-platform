from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.categories.models import Category


async def get_category(db: AsyncSession, category_id: UUID) -> Category | None:
    return await db.get(Category, category_id)


async def get_category_by_slug(db: AsyncSession, slug: str) -> Category | None:
    result = await db.execute(select(Category).where(Category.slug == slug))
    return result.scalar_one_or_none()


async def list_categories(
    db: AsyncSession,
    *,
    include_inactive: bool = False,
) -> list[Category]:
    statement = select(Category)

    if not include_inactive:
        statement = statement.where(Category.active.is_(True))

    statement = statement.order_by(Category.sort_order.asc(), Category.name.asc())
    result = await db.execute(statement)
    return list(result.scalars().all())


async def create_category(db: AsyncSession, data: dict) -> Category:
    category = Category(**data)

    db.add(category)
    await db.commit()
    await db.refresh(category)

    return category


async def update_category(
    db: AsyncSession,
    category: Category,
    data: dict,
) -> Category:
    for field, value in data.items():
        setattr(category, field, value)

    await db.commit()
    await db.refresh(category)

    return category


async def count_children(db: AsyncSession, category_id: UUID) -> int:
    result = await db.execute(
        select(func.count()).select_from(Category).where(Category.parent_id == category_id)
    )
    return result.scalar_one()


async def deactivate_category(
    db: AsyncSession,
    category: Category,
) -> Category:
    category.active = False

    await db.commit()
    await db.refresh(category)

    return category
