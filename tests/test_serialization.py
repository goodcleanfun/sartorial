import json
from datetime import date, datetime, time, timedelta

from dorsal.serialization import Serializable, decode_object, encode_object


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


def test_custom_type():
    class CustomType(Serializable):
        def __init__(self, value):
            if not isinstance(value, str):
                value = str(value)
            self.value = value

        def __str__(self) -> str:
            return "custom:" + self.value

    assert encode_object(CustomType("value")) == "custom:value"
    assert encode_object(CustomType(123)) == "custom:123"
    decoded = decode_object(CustomType, encode_object(CustomType("value")))
    assert isinstance(decoded, CustomType)
    assert decoded.value == "custom:value"
