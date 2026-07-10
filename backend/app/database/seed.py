import asyncio

from sqlalchemy import or_, select

from app.auth.security import hash_password
from app.config.settings import settings
from app.database.session import SessionFactory
from app.geography.models import Country, Region
from app.trust.models import TrustProfile
from app.trust.service import create_trust_profile
from app.users.models import User

REGIONS = (
    ("africa", "Africa"),
    ("asia", "Asia"),
    ("europe", "Europe"),
    ("north-america", "North America"),
    ("oceania", "Oceania"),
    ("south-america", "South America"),
)

# Initial launch and expansion markets. ISO codes are ISO 3166-1 alpha-3.
COUNTRIES = (
    ("GBR", "United Kingdom", "united-kingdom", "GBP", "europe"),
    ("IRL", "Ireland", "ireland", "EUR", "europe"),
    ("FRA", "France", "france", "EUR", "europe"),
    ("DEU", "Germany", "germany", "EUR", "europe"),
    ("ESP", "Spain", "spain", "EUR", "europe"),
    ("USA", "United States", "united-states", "USD", "north-america"),
    ("CAN", "Canada", "canada", "CAD", "north-america"),
    ("BRA", "Brazil", "brazil", "BRL", "south-america"),
    ("NGA", "Nigeria", "nigeria", "NGN", "africa"),
    ("ZAF", "South Africa", "south-africa", "ZAR", "africa"),
    ("IND", "India", "india", "INR", "asia"),
    ("SGP", "Singapore", "singapore", "SGD", "asia"),
    ("AUS", "Australia", "australia", "AUD", "oceania"),
    ("NZL", "New Zealand", "new-zealand", "NZD", "oceania"),
)


async def seed() -> None:
    async with SessionFactory() as session:
        regions_by_slug: dict[str, Region] = {}
        for slug, name in REGIONS:
            region = await session.scalar(select(Region).where(Region.slug == slug))
            if region is None:
                region = Region(slug=slug, name=name)
                session.add(region)
                await session.flush()
            regions_by_slug[slug] = region

        for iso_code, name, slug, currency, region_code in COUNTRIES:
            existing_country = await session.scalar(
                select(Country).where(
                    or_(
                        Country.iso_code == iso_code,
                        Country.slug == slug,
                        Country.name == name,
                    )
                )
            )
            if existing_country is None:
                session.add(
                    Country(
                        iso_code=iso_code,
                        name=name,
                        slug=slug,
                        currency=currency,
                        region_id=regions_by_slug[region_code].id,
                    )
                )
            else:
                existing_country.iso_code = iso_code
                existing_country.slug = slug
                existing_country.currency = currency
                existing_country.region_id = regions_by_slug[region_code].id

        existing = await session.scalar(select(User).where(User.email == settings.seed_admin_email))
        if existing is None:
            existing = User(
                email=settings.seed_admin_email,
                hashed_password=hash_password(settings.seed_admin_password),
                is_admin=True,
            )
            session.add(existing)
            await session.flush()
        trust_profile = await session.scalar(
            select(TrustProfile).where(TrustProfile.user_id == existing.id)
        )
        if trust_profile is None:
            await create_trust_profile(session, existing.id)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())
