from decimal import Decimal

from dorsal.schema import Schema
from dorsal.serialization import Serializable
from dorsal.types import JSONSchemaFormatted


def test_custom_type_schema():
    class CustomTypeA(JSONSchemaFormatted, Serializable):
        schema_format = "custom-a"

        def __init__(self, value) -> None:
            if not isinstance(value, str):
                value = str(value)
            self.value = value

        def __str__(self) -> str:
            return self.value

    class Model(Schema):
        custom: CustomTypeA
        i: int
        f: float
        s: str
        d: Decimal

    schema = Model.to_schema_dict()
    NewModel = Schema.from_schema_dict(schema)
    assert NewModel.__annotations__ == Model.__annotations__
    n = NewModel(custom="value", i=1, f=1.0, s="string", d="1.0")
    assert isinstance(n.custom, CustomTypeA)
    assert n.custom.value == "value"
    assert isinstance(n.d, Decimal)
    assert n.d == Decimal("1.0")
