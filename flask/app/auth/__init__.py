from flask import Blueprint
from app.auth.views import auth_view, registration_view

# Define blueprint that will be registered by main app
auth_api = Blueprint("auth_api", __name__)
auth_view.AuthView.register(auth_api)
registration_view.RegistrationView.register(auth_api)
