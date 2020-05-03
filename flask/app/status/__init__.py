from flask import Blueprint
from app.status.views import health_check_view

# Define blueprint that will be registered by main app
status_api = Blueprint("status_api", __name__)
health_check_view.HealthCheckView.register(status_api)
