import re
import unicodedata

_NON_ALPHANUMERIC_PATTERN = re.compile(r"[^a-z0-9]+")
_REPEATED_DASH_PATTERN = re.compile(r"-+")


def generate_slug(name: str) -> str:
    normalized = unicodedata.normalize("NFKD", name)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    lowercase = ascii_text.lower().strip()
    dashed = _NON_ALPHANUMERIC_PATTERN.sub("-", lowercase)
    return _REPEATED_DASH_PATTERN.sub("-", dashed).strip("-")
