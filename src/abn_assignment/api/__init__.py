from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def _():
        return "hi"

    return app
