from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.geography.models import City, Country, Region
from app.geography.schemas import CityCreate, CountryCreate, RegionCreate


class GeographyConflictError(Exception):
    pass


class RegionNotFoundError(Exception):
    pass


class CountryNotFoundError(Exception):
    pass


async def create_region(db: AsyncSession, payload: RegionCreate) -> Region:
    region = Region(**payload.model_dump())
    db.add(region)
    try:
        await db.commit()
    except IntegrityError as error:
        await db.rollback()
        raise GeographyConflictError("Region already exists") from error
    await db.refresh(region)
    return region


async def list_regions(db: AsyncSession) -> list[Region]:
    result = await db.execute(select(Region).where(Region.active.is_(True)))
    return list(result.scalars().all())


async def create_country(db: AsyncSession, payload: CountryCreate) -> Country:
    region = await db.get(Region, payload.region_id)
    if region is None:
        raise RegionNotFoundError("Region does not exist")

    country = Country(**payload.model_dump())
    db.add(country)
    try:
        await db.commit()
    except IntegrityError as error:
        await db.rollback()
        raise GeographyConflictError("Country already exists") from error
    await db.refresh(country)
    return country


async def list_countries(db: AsyncSession) -> list[Country]:
    result = await db.execute(select(Country).where(Country.active.is_(True)))
    return list(result.scalars().all())


async def list_countries_by_region(db: AsyncSession, region_id) -> list[Country]:
    result = await db.execute(
        select(Country).where(
            Country.region_id == region_id,
            Country.active.is_(True),
        )
    )
    return list(result.scalars().all())


async def create_city(db: AsyncSession, payload: CityCreate) -> City:
    country = await db.get(Country, payload.country_id)
    if country is None:
        raise CountryNotFoundError("Country does not exist")

    city = City(**payload.model_dump())
    db.add(city)
    try:
        await db.commit()
    except IntegrityError as error:
        await db.rollback()
        raise GeographyConflictError("City already exists") from error
    await db.refresh(city)
    return city


async def list_cities_by_country(db: AsyncSession, country_id) -> list[City]:
    result = await db.execute(
        select(City).where(
            City.country_id == country_id,
            City.active.is_(True),
        )
    )
    return list(result.scalars().all())
