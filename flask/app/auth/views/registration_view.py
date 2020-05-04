from flask import request
from flask_classful import route
from app.common.views import BaseView
from app.auth.schemas import AuthUserSchema


class RegistrationView(BaseView):
    route_base = "/"

    @route("/registration/", methods=["POST"])
    def registration(self):
        """ Register new auth users """

        auth_input = self.load_input_data(AuthUserSchema(), request.json)

        return auth_input, 200
