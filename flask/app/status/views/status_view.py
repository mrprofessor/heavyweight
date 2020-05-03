from flask_classful import FlaskView


class StatusView(FlaskView):
    def index(self):
        return "Hello heavyweight"
