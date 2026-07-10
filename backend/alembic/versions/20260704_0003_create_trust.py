"""create 1stKings Trust tables"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260704_0003"
down_revision: str | None = "20260701_0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "trust_profiles",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("trust_id", sa.String(length=50), nullable=False),
        sa.Column("trust_score", sa.Integer(), nullable=False),
        sa.Column("identity_verified", sa.Boolean(), nullable=False),
        sa.Column("email_verified", sa.Boolean(), nullable=False),
        sa.Column("phone_verified", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.CheckConstraint("trust_score BETWEEN 0 AND 100"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("trust_id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index("ix_trust_profiles_trust_id", "trust_profiles", ["trust_id"], unique=True)
    op.create_index("ix_trust_profiles_user_id", "trust_profiles", ["user_id"], unique=True)

    op.create_table(
        "business_verifications",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("owner_id", sa.Uuid(), nullable=False),
        sa.Column("business_name", sa.String(length=255), nullable=False),
        sa.Column("registration_number", sa.String(length=100)),
        sa.Column("address", sa.Text()),
        sa.Column("website", sa.String(length=255)),
        sa.Column("verification_status", sa.String(length=30), nullable=False),
        sa.Column("verified_by_admin", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["owner_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_business_verifications_owner_id",
        "business_verifications",
        ["owner_id"],
    )

    op.create_table(
        "trust_events",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("event_type", sa.String(length=100), nullable=False),
        sa.Column("points", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_trust_events_user_id", "trust_events", ["user_id"])

    op.create_table(
        "reviews",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("reviewer_id", sa.Uuid(), nullable=False),
        sa.Column("business_id", sa.Uuid(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.Text()),
        sa.Column("verified_order", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.CheckConstraint("rating BETWEEN 1 AND 5"),
        sa.ForeignKeyConstraint(["reviewer_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_reviews_business_id", "reviews", ["business_id"])
    op.create_index("ix_reviews_reviewer_id", "reviews", ["reviewer_id"])


def downgrade() -> None:
    op.drop_index("ix_reviews_reviewer_id", table_name="reviews")
    op.drop_index("ix_reviews_business_id", table_name="reviews")
    op.drop_table("reviews")
    op.drop_index("ix_trust_events_user_id", table_name="trust_events")
    op.drop_table("trust_events")
    op.drop_index("ix_business_verifications_owner_id", table_name="business_verifications")
    op.drop_table("business_verifications")
    op.drop_index("ix_trust_profiles_user_id", table_name="trust_profiles")
    op.drop_index("ix_trust_profiles_trust_id", table_name="trust_profiles")
    op.drop_table("trust_profiles")
