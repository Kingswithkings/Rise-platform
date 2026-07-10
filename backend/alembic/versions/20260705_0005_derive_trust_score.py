"""derive Trust scores from events instead of storing them"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260705_0005"
down_revision: str | None = "20260705_0004"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_column("trust_profiles", "trust_score")


def downgrade() -> None:
    op.add_column(
        "trust_profiles",
        sa.Column("trust_score", sa.Integer(), server_default="50", nullable=False),
    )
