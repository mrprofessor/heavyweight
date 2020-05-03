from flask_classful import route
from app.common.views import BaseView


class RegistrationView(BaseView):
    route_base = "/"

    @route("/registration/", methods=["GET"])
    def registration(self):
        return {"yo": "this is registration api"}, 200
