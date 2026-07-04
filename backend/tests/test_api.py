from app.main import app


def test_openapi_is_available() -> None:
    schema = app.openapi()
    assert schema["info"]["title"] == "RISE API"
