BASE_TRUST_SCORE = 50

TRUST_POINTS = {
    "email_verified": 10,
    "phone_verified": 10,
    "business_profile_completed": 10,
    "business_verified": 20,
    "completed_order": 10,
    "positive_review": 5,
    "dispute_report": -20,
    "fraud_report": -40,
}


def calculate_trust_score(events: list[dict]) -> int:
    score = BASE_TRUST_SCORE

    for event in events:
        points = event.get("points", 0)
        score += points

    return max(0, min(score, 100))
