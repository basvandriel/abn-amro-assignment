import click
from abn_assignment.domain.country.service import CountryService

from .constants import USING_YEAR_DATA

from .sql_database import database

from .api import create_app


@click.command()
def populate():
    """
    Program that populates a SQL database with GDP and StackOverflow from 2021.
    """
    click.echo(f"Fetching GDP data from {USING_YEAR_DATA}")

    with create_app().app_context():
        CountryService(database.session).fetch_gdp_data(USING_YEAR_DATA)
