from sqlalchemy.orm import registry, relationship
from .country import Country
from .developer import Developer

from .sql_tables import country_table, developer_table

sql_registry = registry()


def map():
    sql_registry.map_imperatively(
        Country,
        country_table,
        properties={
            "developers": relationship(Developer, backref="developer"),
        },
    )
    sql_registry.map_imperatively(Developer, developer_table)
