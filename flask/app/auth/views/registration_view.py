from flask import request
from flask_classful import route
from app.common.views import BaseView
from app.auth.schemas import AuthUserSchema
from app.auth.services import AuthRegistrationService


class RegistrationView(BaseView):
    route_base = "/"

    @route("/registration/", methods=["POST"])
    def registration(self):
        """ Register new auth users """

        auth_input = self.load_input_data(AuthUserSchema(), request.json)
        registration_data = AuthRegistrationService.auth_user_registration(auth_input)
        return registration_data, 200
