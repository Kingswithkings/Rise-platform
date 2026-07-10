import pytest

from app.trust.trust_score import calculate_trust_score


@pytest.mark.parametrize(
    ("events", "expected"),
    [
        ([], 50),
        ([{"points": 10}], 60),
        ([{"points": 10}, {"points": 10}, {"points": 20}], 90),
        ([{"points": -40}], 10),
        ([{"points": 100}], 100),
        ([{"points": -100}], 0),
    ],
)
def test_calculate_trust_score_is_event_driven_and_bounded(
    events: list[dict[str, int]],
    expected: int,
) -> None:
    assert calculate_trust_score(events) == expected
