from marshmallow import Schema, fields
import re


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class BaseSchema(Schema):
    """
        - We will be using camel case as it's the JSON standard but in python
          code we will keep using the snake-case as it's more convenient.
        - This Base schema that uses camel-case for its external representation
          and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)
