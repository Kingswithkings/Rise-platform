import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.session import get_session
from app.trust.badge import get_badge
from app.trust.models import BusinessVerification, Review, TrustEvent, TrustProfile
from app.trust.schemas import (
    BusinessVerificationCreate,
    BusinessVerificationResponse,
    ReviewCreate,
    ReviewResponse,
    TrustBadgeResponse,
    TrustEventResponse,
    TrustProfileResponse,
)
from app.trust.service import add_trust_event, calculate_user_trust_score
from app.trust.trust_score import TRUST_POINTS
from app.users.models import User

router = APIRouter(prefix="/trust", tags=["1stKings Trust"])
SessionDependency = Annotated[AsyncSession, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


def trust_profile_response(profile: TrustProfile, score: int) -> TrustProfileResponse:
    return TrustProfileResponse(
        id=profile.id,
        user_id=profile.user_id,
        trust_id=profile.trust_id,
        trust_score=score,
        identity_verified=profile.identity_verified,
        email_verified=profile.email_verified,
        phone_verified=profile.phone_verified,
    )


@router.get("/profile/me", response_model=TrustProfileResponse)
async def get_my_trust_profile(
    session: SessionDependency,
    current_user: CurrentUser,
) -> TrustProfileResponse:
    profile = await session.scalar(
        select(TrustProfile).where(TrustProfile.user_id == current_user.id)
    )
    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trust profile not found")
    score = await calculate_user_trust_score(session, current_user.id)
    return trust_profile_response(profile, score)


@router.post(
    "/business-verification",
    response_model=BusinessVerificationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def submit_business_verification(
    payload: BusinessVerificationCreate,
    session: SessionDependency,
    current_user: CurrentUser,
) -> BusinessVerification:
    verification = BusinessVerification(
        owner_id=current_user.id,
        business_name=payload.business_name,
        registration_number=payload.registration_number,
        address=payload.address,
        website=str(payload.website) if payload.website else None,
    )
    session.add(verification)
    await session.commit()
    await session.refresh(verification)
    return verification


@router.get("/events/me", response_model=list[TrustEventResponse])
async def get_my_trust_events(
    session: SessionDependency,
    current_user: CurrentUser,
) -> list[TrustEvent]:
    events = await session.scalars(
        select(TrustEvent)
        .where(TrustEvent.user_id == current_user.id)
        .order_by(TrustEvent.created_at.desc())
    )
    return list(events)


@router.post("/review", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    payload: ReviewCreate,
    session: SessionDependency,
    current_user: CurrentUser,
) -> Review:
    review = Review(
        reviewer_id=current_user.id,
        business_id=payload.business_id,
        rating=payload.rating,
        comment=payload.comment,
        verified_order=False,
    )
    session.add(review)
    await session.commit()
    await session.refresh(review)
    return review


@router.get("/reviews/{business_id}", response_model=list[ReviewResponse])
async def get_business_reviews(
    business_id: uuid.UUID,
    session: SessionDependency,
) -> list[Review]:
    reviews = await session.scalars(
        select(Review).where(Review.business_id == business_id).order_by(Review.created_at.desc())
    )
    return list(reviews)


@router.patch(
    "/admin/verify-business/{verification_id}",
    response_model=BusinessVerificationResponse,
)
async def verify_business(
    verification_id: uuid.UUID,
    session: SessionDependency,
    current_user: CurrentUser,
) -> BusinessVerification:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    verification = await session.get(BusinessVerification, verification_id)
    if verification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business verification not found",
        )

    if not verification.verified_by_admin:
        verification.verification_status = "approved"
        verification.verified_by_admin = True

        await add_trust_event(
            session=session,
            user_id=verification.owner_id,
            event_type="business_verified",
            points=TRUST_POINTS["business_verified"],
            description="Business verified by 1stKings Trust admin",
        )
    await session.commit()
    await session.refresh(verification)
    return verification


@router.patch("/verify/email", response_model=TrustProfileResponse)
async def verify_email(
    session: SessionDependency,
    current_user: CurrentUser,
) -> TrustProfileResponse:
    profile = await session.scalar(
        select(TrustProfile).where(TrustProfile.user_id == current_user.id)
    )
    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trust profile not found",
        )

    if not profile.email_verified:
        profile.email_verified = True
        await add_trust_event(
            session=session,
            user_id=current_user.id,
            event_type="email_verified",
            points=TRUST_POINTS["email_verified"],
            description="Email verified",
        )

    await session.commit()
    await session.refresh(profile)
    score = await calculate_user_trust_score(session, current_user.id)
    return trust_profile_response(profile, score)


@router.patch("/verify/phone", response_model=TrustProfileResponse)
async def verify_phone(
    session: SessionDependency,
    current_user: CurrentUser,
) -> TrustProfileResponse:
    profile = await session.scalar(
        select(TrustProfile).where(TrustProfile.user_id == current_user.id)
    )
    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trust profile not found",
        )

    if not profile.phone_verified:
        profile.phone_verified = True
        await add_trust_event(
            session=session,
            user_id=current_user.id,
            event_type="phone_verified",
            points=TRUST_POINTS["phone_verified"],
            description="Phone verified",
        )

    await session.commit()
    await session.refresh(profile)
    score = await calculate_user_trust_score(session, current_user.id)
    return trust_profile_response(profile, score)


@router.get("/badge/me", response_model=TrustBadgeResponse)
async def get_my_badge(
    session: SessionDependency,
    current_user: CurrentUser,
) -> TrustBadgeResponse:
    profile = await session.scalar(
        select(TrustProfile).where(TrustProfile.user_id == current_user.id)
    )
    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trust profile not found",
        )

    verification = await session.scalar(
        select(BusinessVerification).where(
            BusinessVerification.owner_id == current_user.id,
            BusinessVerification.verified_by_admin.is_(True),
        )
    )
    score = await calculate_user_trust_score(session, current_user.id)
    badge = get_badge(score)
    business_verified = verification is not None
    return TrustBadgeResponse(
        trust_id=profile.trust_id,
        trust_score=score,
        badge=badge,
        badge_label=f"1stKings Trust {badge} Badge",
        verification_label="Verified by 1stKings Trust" if business_verified else None,
        email_verified=profile.email_verified,
        phone_verified=profile.phone_verified,
        identity_verified=profile.identity_verified,
        business_verified=business_verified,
    )
