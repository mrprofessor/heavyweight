from flask import request, make_response, jsonify
from flask import current_app as app
from flask_classful import FlaskView

from app.common.representations.default import output_json


class BaseView(FlaskView):
    # These can be defined by subclass views to
    # opt-out of authentication or authorization
    # as needed, ex ["status_api.HealthView:index"]

    representations = {"application/json": output_json}

    authorization_exempt = []
    authentication_exempt = []

    def parse_url_params(self):
        r_params = {
            "and": {
                k.replace("_and_", ""): v
                for k, v in request.args.items()
                if k.startswith("_and_")
            },
            "in": {
                k.replace("_in_", ""): [i for i in v.split(",") if i]
                for k, v in request.args.items()
                if k.startswith("_in_")
            },
        }
        return r_params
