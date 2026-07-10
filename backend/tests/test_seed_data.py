from app.database.seed import COUNTRIES, REGIONS


def test_reference_seed_data_has_unique_codes_and_valid_regions() -> None:
    region_slugs = {slug for slug, _ in REGIONS}
    country_iso_codes = [iso_code for iso_code, _, _, _, _ in COUNTRIES]

    assert region_slugs == {
        "africa",
        "asia",
        "europe",
        "north-america",
        "oceania",
        "south-america",
    }
    assert len(country_iso_codes) == len(set(country_iso_codes))
    assert all(region_slug in region_slugs for _, _, _, _, region_slug in COUNTRIES)
    assert "GBR" in country_iso_codes
