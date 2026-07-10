"""upgrade geography schema for RISE marketplace"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260710_0006"
down_revision: str | None = "0b1f225db134"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("regions", sa.Column("slug", sa.String(length=120), nullable=True))
    op.add_column(
        "regions",
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.add_column(
        "regions",
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.add_column("regions", sa.Column("updated_at", sa.DateTime(timezone=True)))
    op.execute("UPDATE regions SET slug = lower(replace(name, ' ', '-')) WHERE slug IS NULL")
    op.alter_column("regions", "slug", nullable=False)
    op.create_index("ix_regions_slug", "regions", ["slug"], unique=True)
    op.create_index("ix_regions_name", "regions", ["name"], unique=False)

    op.add_column("countries", sa.Column("slug", sa.String(length=120), nullable=True))
    op.add_column("countries", sa.Column("iso_code", sa.String(length=3), nullable=True))
    op.add_column("countries", sa.Column("currency", sa.String(length=3), nullable=True))
    op.add_column(
        "countries",
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.add_column(
        "countries",
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.add_column("countries", sa.Column("updated_at", sa.DateTime(timezone=True)))
    op.execute(
        """
        UPDATE countries
        SET
            slug = lower(replace(name, ' ', '-')),
            iso_code = code
        WHERE slug IS NULL
        """
    )
    op.alter_column("countries", "slug", nullable=False)
    op.create_index("ix_countries_slug", "countries", ["slug"], unique=True)
    op.create_index("ix_countries_name", "countries", ["name"], unique=False)

    op.create_table(
        "cities",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("country_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True)),
        sa.ForeignKeyConstraint(["country_id"], ["countries.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_cities_country_id", "cities", ["country_id"], unique=False)
    op.create_index("ix_cities_name", "cities", ["name"], unique=False)
    op.create_index("ix_cities_slug", "cities", ["slug"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_cities_slug", table_name="cities")
    op.drop_index("ix_cities_name", table_name="cities")
    op.drop_index("ix_cities_country_id", table_name="cities")
    op.drop_table("cities")

    op.drop_index("ix_countries_name", table_name="countries")
    op.drop_index("ix_countries_slug", table_name="countries")
    op.drop_column("countries", "updated_at")
    op.drop_column("countries", "created_at")
    op.drop_column("countries", "active")
    op.drop_column("countries", "currency")
    op.drop_column("countries", "iso_code")
    op.drop_column("countries", "slug")

    op.drop_index("ix_regions_name", table_name="regions")
    op.drop_index("ix_regions_slug", table_name="regions")
    op.drop_column("regions", "updated_at")
    op.drop_column("regions", "created_at")
    op.drop_column("regions", "active")
    op.drop_column("regions", "slug")
