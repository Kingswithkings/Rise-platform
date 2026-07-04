"""create geographic reference tables"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260701_0002"
down_revision: str | None = "20260701_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "regions",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
        sa.UniqueConstraint("name"),
    )
    op.create_index("ix_regions_code", "regions", ["code"], unique=True)

    op.create_table(
        "countries",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("region_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["region_id"], ["regions.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
        sa.UniqueConstraint("name"),
    )
    op.create_index("ix_countries_code", "countries", ["code"], unique=True)
    op.create_index("ix_countries_region_id", "countries", ["region_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_countries_region_id", table_name="countries")
    op.drop_index("ix_countries_code", table_name="countries")
    op.drop_table("countries")
    op.drop_index("ix_regions_code", table_name="regions")
    op.drop_table("regions")
