"""add concurrency-safe Trust ID sequence and backfill profiles"""

import uuid
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260705_0004"
down_revision: str | None = "20260704_0003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    connection = op.get_bind()
    op.execute(sa.text("CREATE SEQUENCE trust_id_sequence START WITH 1"))

    users = connection.execute(
        sa.text(
            """
            SELECT users.id
            FROM users
            LEFT JOIN trust_profiles ON trust_profiles.user_id = users.id
            WHERE trust_profiles.id IS NULL
            ORDER BY users.created_at, users.id
            """
        )
    )
    existing_count = connection.scalar(sa.text("SELECT count(*) FROM trust_profiles")) or 0
    next_number = existing_count + 1
    for user in users:
        connection.execute(
            sa.text(
                """
                INSERT INTO trust_profiles (
                    id, user_id, trust_id, trust_score, identity_verified,
                    email_verified, phone_verified
                )
                VALUES (
                    :id, :user_id, :trust_id, 50, false, false, false
                )
                """
            ),
            {
                "id": uuid.uuid4(),
                "user_id": user.id,
                "trust_id": f"KT-2026-{next_number:06d}",
            },
        )
        next_number += 1

    allocated = next_number - 1
    if allocated:
        connection.execute(
            sa.text("SELECT setval('trust_id_sequence', :value, true)"),
            {"value": allocated},
        )


def downgrade() -> None:
    op.execute(sa.text("DROP SEQUENCE trust_id_sequence"))
