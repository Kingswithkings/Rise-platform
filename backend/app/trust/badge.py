def get_badge(score: int) -> str:
    if score >= 95:
        return "Elite"

    if score >= 85:
        return "Verified"

    if score >= 70:
        return "Trusted"

    if score >= 50:
        return "Standard"

    return "New"
