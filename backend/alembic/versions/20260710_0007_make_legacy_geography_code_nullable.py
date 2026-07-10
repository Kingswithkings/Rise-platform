"""make legacy geography code columns nullable"""

from collections.abc import Sequence

from alembic import op

revision: str = "20260710_0007"
down_revision: str | None = "20260710_0006"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column("regions", "code", nullable=True)
    op.alter_column("countries", "code", nullable=True)


def downgrade() -> None:
    op.alter_column("countries", "code", nullable=False)
    op.alter_column("regions", "code", nullable=False)
