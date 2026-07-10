import uuid
from datetime import UTC, datetime

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.trust.models import TrustEvent, TrustProfile
from app.trust.trust_score import calculate_trust_score


def generate_trust_id(sequence_number: int) -> str:
    return f"KT-{datetime.now(UTC).year}-{sequence_number:06d}"


async def create_trust_profile(session: AsyncSession, user_id: uuid.UUID) -> TrustProfile:
    sequence_number = await session.scalar(text("SELECT nextval('trust_id_sequence')"))
    if sequence_number is None:
        raise RuntimeError("Unable to allocate Trust ID")
    trust_profile = TrustProfile(
        user_id=user_id,
        trust_id=generate_trust_id(sequence_number),
    )
    session.add(trust_profile)
    await session.flush()
    return trust_profile


async def add_trust_event(
    session: AsyncSession,
    user_id: uuid.UUID,
    event_type: str,
    points: int,
    description: str | None = None,
) -> TrustEvent:
    event = TrustEvent(
        user_id=user_id,
        event_type=event_type,
        points=points,
        description=description,
    )
    session.add(event)
    await session.flush()
    return event


async def calculate_user_trust_score(
    session: AsyncSession,
    user_id: uuid.UUID,
) -> int:
    events = await session.scalars(select(TrustEvent).where(TrustEvent.user_id == user_id))
    event_data = [{"event_type": event.event_type, "points": event.points} for event in events]

    return calculate_trust_score(event_data)
