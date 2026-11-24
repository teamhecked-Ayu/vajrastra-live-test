"""Small disposable service used for Vajrastra's live workflow test."""


def parse_timeout(value: str) -> int:
    """Parse a timeout and require a positive integer."""
    try:
        timeout = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("timeout must be an integer") from exc
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    return timeout
