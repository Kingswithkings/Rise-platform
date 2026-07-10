import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class TrustSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TrustProfileResponse(TrustSchema):
    id: uuid.UUID
    user_id: uuid.UUID
    trust_id: str
    trust_score: int
    identity_verified: bool
    email_verified: bool
    phone_verified: bool


class TrustBadgeResponse(BaseModel):
    trust_id: str
    trust_score: int
    badge: Literal["Elite", "Verified", "Trusted", "Standard", "New"]
    badge_label: str
    verification_label: Literal["Verified by 1stKings Trust"] | None
    email_verified: bool
    phone_verified: bool
    identity_verified: bool
    business_verified: bool


class BusinessVerificationCreate(BaseModel):
    business_name: str = Field(min_length=1, max_length=255)
    registration_number: str | None = Field(default=None, max_length=100)
    address: str | None = None
    website: HttpUrl | None = None


class BusinessVerificationResponse(TrustSchema):
    id: uuid.UUID
    owner_id: uuid.UUID
    business_name: str
    registration_number: str | None
    address: str | None
    website: str | None
    verification_status: str
    verified_by_admin: bool
    created_at: datetime


class TrustEventResponse(TrustSchema):
    id: uuid.UUID
    user_id: uuid.UUID
    event_type: str
    points: int
    description: str | None
    created_at: datetime


class ReviewCreate(BaseModel):
    business_id: uuid.UUID
    rating: int = Field(ge=1, le=5)
    comment: str | None = None


class ReviewResponse(TrustSchema):
    id: uuid.UUID
    reviewer_id: uuid.UUID
    business_id: uuid.UUID
    rating: int
    comment: str | None
    verified_order: bool
    created_at: datetime
