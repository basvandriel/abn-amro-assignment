from flask import Flask
from pytest import fixture
import pytest
from abn_assignment.api import create_app
from abn_assignment.sql_database import database

from sqlalchemy.orm import scoped_session

from flask.testing import FlaskClient


@fixture
def app() -> Flask:
    app = create_app("abnamro_test")
    app.config.update(
        {
            "TESTING": True,
        }
    )
    with app.app_context():
        database.drop_all()
        database.create_all()
        yield app


@pytest.fixture()
def client(app) -> FlaskClient:
    return app.test_client()


@fixture
def sql_session(app: Flask) -> scoped_session:
    return database.session
