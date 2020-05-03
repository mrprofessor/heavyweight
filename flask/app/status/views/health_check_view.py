from flask_classful import FlaskView


class HealthCheckView(FlaskView):
    def index(self):
        return "Hello heavyweight"
