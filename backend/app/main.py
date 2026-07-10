from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis.asyncio import Redis
from sqlalchemy import text

from app.auth.routes import router as auth_router
from app.config.settings import settings
from app.core.logging import configure_logging
from app.database.session import SessionFactory, engine
from app.geography.router import router as geography_router
from app.trust.router import router as trust_router

configure_logging()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await engine.dispose()


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(trust_router, prefix="/api/v1")
app.include_router(geography_router, prefix="/api/v1")


@app.get("/health", tags=["operations"])
async def health() -> dict[str, str]:
    async with SessionFactory() as session:
        await session.execute(text("SELECT 1"))
    redis = Redis.from_url(settings.redis_url)
    try:
        await redis.ping()
    finally:
        await redis.aclose()
    return {"status": "healthy"}
