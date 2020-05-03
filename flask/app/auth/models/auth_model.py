from app import db
from app.common.models.base import BaseModel


class AuthModel(BaseModel):
    __abstract__ = True
    __bind_key__ = "authorization"
