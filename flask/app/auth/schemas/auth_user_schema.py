from app.common.schemas import BaseSchema, fields


class AuthUserSchema(BaseSchema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
