"""Small disposable service used for Vajrastra's live workflow test."""


def parse_timeout(value: str) -> int:
    """Parse a timeout value. Positive-range validation is the test task."""
    return int(value)
