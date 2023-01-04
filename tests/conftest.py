from flask import Flask
from pytest import fixture
from abn_assignment.api import create_app
from abn_assignment.sql_database import database

from sqlalchemy.orm import scoped_session


@fixture
def app() -> Flask:
    with create_app("abnamro_test").app_context():
        yield app


@fixture
def sql_session(app: Flask) -> scoped_session:
    database.drop_all()
    database.create_all()
    return database.session
