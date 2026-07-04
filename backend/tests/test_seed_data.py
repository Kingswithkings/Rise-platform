from app.database.seed import COUNTRIES, REGIONS


def test_reference_seed_data_has_unique_codes_and_valid_regions() -> None:
    region_codes = {code for code, _ in REGIONS}
    country_codes = [code for code, _, _ in COUNTRIES]

    assert region_codes == {"AF", "AS", "EU", "NA", "OC", "SA"}
    assert len(country_codes) == len(set(country_codes))
    assert all(region_code in region_codes for _, _, region_code in COUNTRIES)
    assert "GB" in country_codes
