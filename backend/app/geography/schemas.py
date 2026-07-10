from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RegionCreate(BaseModel):
    name: str
    slug: str


class RegionResponse(RegionCreate):
    id: UUID
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CountryCreate(BaseModel):
    region_id: UUID
    name: str
    slug: str
    iso_code: str | None = None
    currency: str | None = None


class CountryResponse(CountryCreate):
    id: UUID
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CityCreate(BaseModel):
    country_id: UUID
    name: str
    slug: str


class CityResponse(CityCreate):
    id: UUID
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True
