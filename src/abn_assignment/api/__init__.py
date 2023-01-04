from flask import Flask

from abn_assignment.constants import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)
from ..sql_database import database
from ..sql_registry import map as map_registry

from ..domain.country.blueprint import blueprint


def create_app(database_name: str = DATABASE_NAME) -> Flask:
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"""
    postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}
    """.strip()
    database.init_app(app)
    map_registry()

    app.register_blueprint(blueprint)
    return app
