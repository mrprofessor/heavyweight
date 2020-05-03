from flask import Flask
from flask_cors import CORS


def register_blueprints(app):
    """ Register all API blueprints here """
    from app.status import status_api

    app.register_blueprint(status_api, url_prefix="/api/")


def create_app(flask_config_name=None, **kwargs):
    app = Flask(__name__, **kwargs)
    # load_config(app, flask_config_name)
    # setup_logging(app.config)
    register_blueprints(app)
    # register_error_handlers(app)
    # init_db(app)
    CORS(app)
    return app
