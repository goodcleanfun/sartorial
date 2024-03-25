import json
from datetime import date, datetime, time, timedelta

from corral.serialization import encode_object


def test_encode_object():
    test_cases = [
        (datetime(2024, 1, 1, 12, 34, 56), "2024-01-01T12:34:56"),
        (date(2024, 1, 1), "2024-01-01"),
        (time(12, 34, 56), "12:34:56"),
        (
            timedelta(hours=12, minutes=34, seconds=56),
            1.0 * (12 * 60 * 60) + (34 * 60) + 56,
        ),
        (12.34, 12.34),
        (18446744073709551615, 18446744073709551615),
        ("string", "string"),
    ]

    for o, e in test_cases:
        assert encode_object(o) == e
        j = f'"{e}"' if isinstance(e, str) else str(e)
        assert json.dumps(o, default=encode_object) == j
