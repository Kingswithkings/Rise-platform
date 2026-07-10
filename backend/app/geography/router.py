from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.geography import repository
from app.geography.schemas import (
    CityCreate,
    CityResponse,
    CountryCreate,
    CountryResponse,
    RegionCreate,
    RegionResponse,
)

router = APIRouter(prefix="/geography", tags=["Geography"])
SessionDependency = Annotated[AsyncSession, Depends(get_session)]


@router.post("/regions", response_model=RegionResponse)
async def create_region(payload: RegionCreate, db: SessionDependency):
    try:
        return await repository.create_region(db, payload)
    except repository.GeographyConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Region already exists",
        ) from error


@router.get("/regions", response_model=list[RegionResponse])
async def list_regions(db: SessionDependency):
    return await repository.list_regions(db)


@router.post("/countries", response_model=CountryResponse)
async def create_country(payload: CountryCreate, db: SessionDependency):
    try:
        return await repository.create_country(db, payload)
    except repository.RegionNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Region not found",
        ) from error
    except repository.GeographyConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Country already exists",
        ) from error


@router.get("/countries", response_model=list[CountryResponse])
async def list_countries(db: SessionDependency):
    return await repository.list_countries(db)


@router.get("/regions/{region_id}/countries", response_model=list[CountryResponse])
async def list_countries_by_region(region_id: UUID, db: SessionDependency):
    return await repository.list_countries_by_region(db, region_id)


@router.post("/cities", response_model=CityResponse)
async def create_city(payload: CityCreate, db: SessionDependency):
    try:
        return await repository.create_city(db, payload)
    except repository.CountryNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Country not found",
        ) from error
    except repository.GeographyConflictError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="City already exists",
        ) from error


@router.get("/countries/{country_id}/cities", response_model=list[CityResponse])
async def list_cities_by_country(country_id: UUID, db: SessionDependency):
    return await repository.list_cities_by_country(db, country_id)
