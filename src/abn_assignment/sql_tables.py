from .sql_database import database
from sqlalchemy import Column, ForeignKey, Integer, String, Float, ARRAY

country_table = database.Table(
    "country",
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String, nullable=False),
    Column("iso_code", String, nullable=False),
    Column("gdp_in_euro", Float, nullable=True),
)

developer_table = database.Table(
    "developer",
    Column("id", Integer, primary_key=True, nullable=False),
    Column("worked_with", ARRAY(String), nullable=False),
    Column("age_range", String, nullable=False),
    Column("country_id", Integer, ForeignKey("country.id"), nullable=False),
)
