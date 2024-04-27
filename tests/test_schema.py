from decimal import Decimal
from typing import Dict, List

from sartorial.schema import Schema
from sartorial.serialization import Serializable
from sartorial.types import JSONSchemaFormatted


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
        custom_list: List[CustomTypeA]
        custom_dict: Dict[str, CustomTypeA]
        i: int
        f: float
        s: str
        d: Decimal

    schema = Model.to_schema_dict()
    NewModel = Schema.from_schema_dict(schema)
    assert NewModel.__annotations__ == Model.__annotations__
    n = NewModel(
        custom="value",
        i=1,
        f=1.0,
        s="string",
        d=1.005678,
        custom_list=["v1", "v2"],
        custom_dict={"k1": "v1", "k2": "v2"},
    )
    assert isinstance(n.custom, CustomTypeA)
    assert n.custom.value == "value"
    assert isinstance(n.d, Decimal)
    assert n.d == Decimal("1.005678")
    assert isinstance(n.custom_list[0], CustomTypeA)
    assert n.custom_list[0].value == "v1"
    assert isinstance(n.custom_dict["k1"], CustomTypeA)
    assert n.custom_dict["k1"].value == "v1"
