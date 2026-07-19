from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.categories import repository
from app.categories.models import Category
from app.categories.schemas import (
    CategoryCreate,
    CategoryTreeResponse,
    CategoryUpdate,
)


async def create_category(
    db: AsyncSession,
    payload: CategoryCreate,
) -> Category:
    if await repository.get_category_by_slug(db, payload.slug):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A category with this slug already exists",
        )

    if payload.parent_id:
        parent = await repository.get_category(db, payload.parent_id)

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent category not found",
            )

        if not parent.active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category is inactive",
            )

    try:
        return await repository.create_category(db, payload.model_dump())
    except IntegrityError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category could not be created",
        ) from exc


async def list_categories(
    db: AsyncSession,
    include_inactive: bool = False,
) -> list[Category]:
    return await repository.list_categories(
        db,
        include_inactive=include_inactive,
    )


async def get_category(db: AsyncSession, category_id: UUID) -> Category:
    category = await repository.get_category(db, category_id)

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


async def update_category(
    db: AsyncSession,
    category_id: UUID,
    payload: CategoryUpdate,
) -> Category:
    category = await get_category(db, category_id)
    update_data = payload.model_dump(exclude_unset=True)

    new_slug = update_data.get("slug")

    if new_slug and new_slug != category.slug:
        existing = await repository.get_category_by_slug(db, new_slug)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A category with this slug already exists",
            )

    if "parent_id" in update_data:
        new_parent_id = update_data["parent_id"]

        if new_parent_id == category.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A category cannot be its own parent",
            )

        if new_parent_id:
            parent = await repository.get_category(db, new_parent_id)

            if not parent:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Parent category not found",
                )

            if await _is_descendant(
                db=db,
                possible_descendant_id=new_parent_id,
                category_id=category.id,
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Circular category hierarchy is not allowed",
                )

    try:
        return await repository.update_category(db, category, update_data)
    except IntegrityError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category could not be updated",
        ) from exc


async def deactivate_category(
    db: AsyncSession,
    category_id: UUID,
) -> Category:
    category = await get_category(db, category_id)

    if await repository.count_children(db, category_id) > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Deactivate child categories before deactivating this category",
        )

    return await repository.deactivate_category(db, category)


async def build_category_tree(db: AsyncSession) -> list[CategoryTreeResponse]:
    categories = await repository.list_categories(db)
    nodes: dict[UUID, CategoryTreeResponse] = {}

    for category in categories:
        nodes[category.id] = _to_tree_response(category)

    roots: list[CategoryTreeResponse] = []

    for category in categories:
        node = nodes[category.id]

        if category.parent_id and category.parent_id in nodes:
            nodes[category.parent_id].children.append(node)
        else:
            roots.append(node)

    return roots


def _to_tree_response(category: Category) -> CategoryTreeResponse:
    return CategoryTreeResponse(
        id=category.id,
        parent_id=category.parent_id,
        name=category.name,
        slug=category.slug,
        description=category.description,
        image_url=category.image_url,
        icon=category.icon,
        sort_order=category.sort_order,
        active=category.active,
        created_at=category.created_at,
        updated_at=category.updated_at,
        children=[],
    )


async def _is_descendant(
    db: AsyncSession,
    possible_descendant_id: UUID,
    category_id: UUID,
) -> bool:
    current = await repository.get_category(db, possible_descendant_id)

    while current:
        if current.parent_id == category_id:
            return True

        if current.parent_id is None:
            return False

        current = await repository.get_category(db, current.parent_id)

    return False
