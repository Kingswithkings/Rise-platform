import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl

from app.stores.models import StoreStatus


class StoreCreate(BaseModel):
    category_id: uuid.UUID
    country_id: uuid.UUID
    city_id: uuid.UUID

    store_name: str = Field(min_length=2, max_length=150)
    slug: str = Field(
        min_length=2,
        max_length=180,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )

    description: str | None = Field(default=None, max_length=5000)
    logo_url: HttpUrl | None = None
    cover_url: HttpUrl | None = None

    email: EmailStr
    phone: str | None = Field(default=None, max_length=40)
    website: HttpUrl | None = None

    address: str = Field(min_length=3, max_length=500)
    postal_code: str | None = Field(default=None, max_length=30)

    latitude: Decimal | None = Field(
        default=None,
        ge=Decimal("-90"),
        le=Decimal("90"),
    )

    longitude: Decimal | None = Field(
        default=None,
        ge=Decimal("-180"),
        le=Decimal("180"),
    )


class StoreUpdate(BaseModel):
    category_id: uuid.UUID | None = None
    country_id: uuid.UUID | None = None
    city_id: uuid.UUID | None = None

    store_name: str | None = Field(default=None, min_length=2, max_length=150)
    slug: str | None = Field(
        default=None,
        min_length=2,
        max_length=180,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )

    description: str | None = Field(default=None, max_length=5000)
    logo_url: HttpUrl | None = None
    cover_url: HttpUrl | None = None

    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=40)
    website: HttpUrl | None = None

    address: str | None = Field(default=None, min_length=3, max_length=500)
    postal_code: str | None = Field(default=None, max_length=30)

    latitude: Decimal | None = Field(
        default=None,
        ge=Decimal("-90"),
        le=Decimal("90"),
    )

    longitude: Decimal | None = Field(
        default=None,
        ge=Decimal("-180"),
        le=Decimal("180"),
    )


class StoreResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    owner_id: uuid.UUID
    category_id: uuid.UUID
    country_id: uuid.UUID
    city_id: uuid.UUID

    store_name: str
    slug: str
    description: str | None

    logo_url: str | None
    cover_url: str | None

    email: str
    phone: str | None
    website: str | None

    address: str
    postal_code: str | None
    latitude: Decimal | None
    longitude: Decimal | None

    status: StoreStatus
    verified: bool
    active: bool
    trust_score: int
    average_rating: Decimal

    created_at: datetime
    updated_at: datetime


class StoreStatusUpdate(BaseModel):
    status: StoreStatus

class StoreListResponse(BaseModel):
    items: list[StoreResponse]
    total: int
    limit: int
    offset: int