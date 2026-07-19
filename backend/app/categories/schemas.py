from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    slug: str = Field(
        min_length=2,
        max_length=140,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )
    description: str | None = None
    image_url: str | None = None
    icon: str | None = None
    sort_order: int = Field(default=0, ge=0)
    active: bool = True


class CategoryCreate(CategoryBase):
    parent_id: UUID | None = None


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    slug: str | None = Field(
        default=None,
        min_length=2,
        max_length=140,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )
    parent_id: UUID | None = None
    description: str | None = None
    image_url: str | None = None
    icon: str | None = None
    sort_order: int | None = Field(default=None, ge=0)
    active: bool | None = None


class CategoryResponse(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    parent_id: UUID | None
    created_at: datetime
    updated_at: datetime


class CategoryTreeResponse(CategoryResponse):
    children: list["CategoryTreeResponse"] = Field(default_factory=list)


CategoryTreeResponse.model_rebuild()
