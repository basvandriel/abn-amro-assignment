from flask import Flask
from pytest import fixture
from abn_assignment.api import create_app
from abn_assignment.sql_database import database

from sqlalchemy.orm import scoped_session


@fixture
def app() -> Flask:
    app = create_app("abnamro_test")

    with app.app_context():
        database.drop_all()
        database.create_all()
        yield app


@fixture
def sql_session(app: Flask) -> scoped_session:
    return database.session
