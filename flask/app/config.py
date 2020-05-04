import os


class Config(object):
    """ Application config options """

    APPNAME = "heavyweight"
    VERSION = "1.0.0"

    def __init__(self):
        self.SECRET_KEY = "heavyweight-string-secret"
        self.DB_USER = "admin"
        self.DB_PASS = "password"
        self.DB_ADDR = "localhost"
        # self.DB_ADDR = "postgres_service"
        self.DB_PORT = "5432"
        self.DB_NAME_MAIN = "heavyweight"
        self.DB_NAME_AUTH = "authorization"
        self.MAIN_DATABASE_URI = Config.get_postgresql_uri(
            self.DB_USER, self.DB_PASS, self.DB_ADDR, self.DB_PORT, self.DB_NAME_MAIN
        )
        self.AUTHZ_DATABASE_URI = Config.get_postgresql_uri(
            self.DB_USER, self.DB_PASS, self.DB_ADDR, self.DB_PORT, self.DB_NAME_AUTH
        )

        self.SQLALCHEMY_BINDS = {
            "heavyweight": self.MAIN_DATABASE_URI,
            "authorization": self.AUTHZ_DATABASE_URI,
        }

        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SQLALCHEMY_NATIVE_UNICODE = True
        self.SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def get_postgresql_uri(
        user: str, password: str, address: str, port: str, name: str
    ):
        return "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            user, password, address, port, name
        )


class DevelopmentConfig(Config):
    """ Dev environment config options """

    def __init__(self):
        super().__init__()

        self.FLASK_ENV = "development"
        self.DEBUG = True
        self.PROFILE = True
        self.SQLALCHEMY_ECHO = True


APP_CONFIG = {"development": DevelopmentConfig}
