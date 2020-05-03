from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    # FIXME
    # We shouldn't import these models manually
    from app.status import models as StatusModels
    from app.auth import models as AuthModels
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """ Register all API blueprints here """
    from app.status import status_api
    from app.auth import auth_api

    app.register_blueprint(status_api, url_prefix="/api/status/")
    app.register_blueprint(auth_api, url_prefix="/api/auth/")


def load_config(app):
    """ Load config for config.py """
    from app.config import DevelopmentConfig

    app.config.from_object(DevelopmentConfig())


def create_app(flask_config_name=None, **kwargs):
    app = Flask(__name__, **kwargs)
    load_config(app)
    register_blueprints(app)
    init_db(app)
    CORS(app)

    # setup_logging(app.config)
    # register_error_handlers(app)
    return app
