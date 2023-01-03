from .sql_database import database
from sqlalchemy import Column, Integer, String, Float

country_table = database.Table(
    "country",
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String, nullable=False),
    Column("iso_code", String, nullable=False),
    Column("gdp_in_euro", Float, nullable=False),
)

developer_table = database.Table(
    "developer",
    Column("id", Integer, primary_key=True, nullable=False),
    Column("worked_with", String, nullable=False),
    Column("age_range", String, nullable=False),
)
