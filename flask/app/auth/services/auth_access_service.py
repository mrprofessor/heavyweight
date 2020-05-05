from app.auth.models import AuthUser
from app.common.exceptions import ServiceException, AuthenticationException
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required


class AuthAccessService:
    @staticmethod
    def auth_user_login(user_data):
        """ Register an auth user and return jwt token """

        current_user = AuthUser.find_by_key(key="username", value=user_data["username"])

        # FIXME
        # Shouln't we just throw AuthenticationException which is more secure?
        if not current_user:
            raise ServiceException(detail=f"User {user_data['username']} doesn't exist")

        if AuthUser.verify_hash(user_data["password"], current_user.password):
            access_token = create_access_token(identity=user_data["username"])
            refresh_token = create_refresh_token(identity=user_data["username"])

            return {
                "message": f"User {user_data['username']} was created.",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        else:
            raise AuthenticationException
