from dorsal.types import JSONSchemaFormatted
from pydantic import BaseModel


def test_json_schema_formatted():
    class CustomType(JSONSchemaFormatted):
        schema_format = "custom"

    class Model(BaseModel):
        custom: CustomType

    schema = Model.model_json_schema()
    assert schema == {
        "title": "Model",
        "type": "object",
        "properties": {
            "custom": {"type": "string", "format": "custom", "title": "Custom"}
        },
        "required": ["custom"],
    }
