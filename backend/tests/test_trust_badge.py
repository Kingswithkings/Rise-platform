import pytest

from app.trust.badge import get_badge


@pytest.mark.parametrize(
    ("score", "badge"),
    [
        (100, "Elite"),
        (95, "Elite"),
        (94, "Verified"),
        (85, "Verified"),
        (84, "Trusted"),
        (70, "Trusted"),
        (69, "Standard"),
        (50, "Standard"),
        (49, "New"),
        (0, "New"),
    ],
)
def test_get_badge_boundaries(score: int, badge: str) -> None:
    assert get_badge(score) == badge
