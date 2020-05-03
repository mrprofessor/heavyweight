from flask_classful import route
from app.common.views import BaseView


class AuthView(BaseView):
    route_base = "/"

    @route("/login/", methods=["GET"])
    def login(self):
        return {"yo": "this is login api"}, 200

    @route("/logout/access/", methods=["GET"])
    def logout_access(self):
        return {"yo": "this is logout access api"}, 200

    @route("/logout/refresh/", methods=["GET"])
    def logout_refresh(self):
        return {"yo": "this is logut refresh api"}, 200

    @route("/token/refresh/", methods=["GET"])
    def token_refresh(self):
        return {"yo": "this is token refresh api"}, 200
