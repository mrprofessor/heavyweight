from flask import request
from flask_classful import route
from app.common.views import BaseView
from app.auth.schemas import AuthUserSchema
from app.auth.services import AuthAccessService
from flask_jwt_extended import (
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    create_access_token,
)


class AuthView(BaseView):
    route_base = "/"

    @route("/login/", methods=["POST"])
    def login(self):
        """ Register new auth users """

        auth_input = self.load_input_data(AuthUserSchema(), request.json)
        login_data = AuthAccessService.auth_user_login(auth_input)
        return login_data, 200

    @route("/token/refresh/", methods=["POST"])
    @jwt_refresh_token_required
    def token_refresh(self):
        # FIXME
        # Move to sevice
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {"access_token": access_token}, 200

    # @route("/logout/access/", methods=["GET"])
    # # @jwt_required
    # def logout_access(self):
    # return {"yo": "this is logout access api"}, 200

    # @route("/logout/refresh/", methods=["GET"])
    # def logout_refresh(self):
    # return {"yo": "this is logut refresh api"}, 200
