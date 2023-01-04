from dotenv import load_dotenv

# import abn_assignment.ap
from abn_assignment.api import create_app
from abn_assignment.sql_database import database

load_dotenv()

with create_app().app_context():
    database.create_all()
