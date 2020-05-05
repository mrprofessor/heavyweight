from app.auth.models import AuthUser
from app.common.exceptions import ServiceException
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required


class AuthRegistrationService:
    @staticmethod
    def auth_user_registration(user_data):
        """ Register an auth user and return jwt token """

        # Check whether the user already exists
        if AuthUser.find_by_key("username", user_data["username"]):
            raise ServiceException(
                detail=f"User {user_data['username']} already exists"
            )

        # Create auth user
        AuthUser.create(
            {
                "username": user_data["username"],
                "password": AuthUser.generate_hash(user_data["password"]),
            }
        )

        access_token = create_access_token(identity=user_data["username"])
        refresh_token = create_refresh_token(identity=user_data["username"])

        return {
            "message": f"User {user_data['username']} was created.",
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
