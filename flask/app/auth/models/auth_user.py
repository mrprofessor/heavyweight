from app import db
from app.auth.models.auth_model import AuthModel
from passlib.hash import pbkdf2_sha256 as sha256


class AuthUser(AuthModel):
    __tablename__ = "auth_user"

    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    # Remove after adding masrshmallow
    @classmethod
    def return_all(cls):
        all_users = AuthUser.read()

        def to_json(x):
            return {"username": x.username, "password": x.password}

        users_dump = [
            {"username": x.username, "password": x.password} for x in all_users
        ]
        return users_dump

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {"message": f"{num_rows_deleted} row(s) deleted"}
        except Exception:
            return {"message": "Something went wrong"}
