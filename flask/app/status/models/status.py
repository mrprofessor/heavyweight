from app import db
from app.common.models.base import BaseModel


class status(BaseModel):
    __tablename__ = "status"

    name = db.Column(db.String(120))
