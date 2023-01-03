from flask import Flask

from abn_assignment.constants import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)
from ..sql_database import database


def create_app() -> Flask:
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"""
    postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}
    """
    database.init_app(app)

    @app.route("/")
    def _():
        return "hi"

    return app
