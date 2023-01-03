from flask import Flask
from pytest import fixture
from abn_assignment.api import create_app
from abn_assignment.sql_database import database


@fixture
def app() -> Flask:
    app = create_app()

    with app.app_context():
        database.create_all()

    return app
