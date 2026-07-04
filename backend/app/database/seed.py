import asyncio

from sqlalchemy import select

from app.auth.security import hash_password
from app.config.settings import settings
from app.countries.models import Country
from app.database.session import SessionFactory
from app.regions.models import Region
from app.users.models import User

REGIONS = (
    ("AF", "Africa"),
    ("AS", "Asia"),
    ("EU", "Europe"),
    ("NA", "North America"),
    ("OC", "Oceania"),
    ("SA", "South America"),
)

# Initial launch and expansion markets. Codes are ISO 3166-1 alpha-2.
COUNTRIES = (
    ("GB", "United Kingdom", "EU"),
    ("IE", "Ireland", "EU"),
    ("FR", "France", "EU"),
    ("DE", "Germany", "EU"),
    ("ES", "Spain", "EU"),
    ("US", "United States", "NA"),
    ("CA", "Canada", "NA"),
    ("BR", "Brazil", "SA"),
    ("NG", "Nigeria", "AF"),
    ("ZA", "South Africa", "AF"),
    ("IN", "India", "AS"),
    ("SG", "Singapore", "AS"),
    ("AU", "Australia", "OC"),
    ("NZ", "New Zealand", "OC"),
)


async def seed() -> None:
    async with SessionFactory() as session:
        regions_by_code: dict[str, Region] = {}
        for code, name in REGIONS:
            region = await session.scalar(select(Region).where(Region.code == code))
            if region is None:
                region = Region(code=code, name=name)
                session.add(region)
                await session.flush()
            regions_by_code[code] = region

        for code, name, region_code in COUNTRIES:
            existing_country = await session.scalar(select(Country).where(Country.code == code))
            if existing_country is None:
                session.add(Country(code=code, name=name, region=regions_by_code[region_code]))

        existing = await session.scalar(select(User).where(User.email == settings.seed_admin_email))
        if existing is None:
            session.add(
                User(
                    email=settings.seed_admin_email,
                    hashed_password=hash_password(settings.seed_admin_password),
                    is_admin=True,
                )
            )
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())
