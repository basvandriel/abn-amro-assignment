import click
from abn_assignment.domain.country.service import CountryService
from abn_assignment.domain.country.sql_repository import SQLCountryRepository
from abn_assignment.domain.developer.sql_repository import (
    SQLDeveloperRepository,
)  # noqa
from abn_assignment.domain.developer.service import Service

from .constants import USING_YEAR_DATA

from .sql_database import database

from .api import create_app


@click.command()
def populate():
    """
    Program that populates a SQL database with GDP and StackOverflow from 2021.
    """
    app = create_app()
    click.echo(f"Fetching GDP data from {USING_YEAR_DATA}")

    country_repo = SQLCountryRepository(database.session)
    developer_repo = SQLDeveloperRepository(database.session)

    country_service = CountryService(country_repo, developer_repo)
    developer_service = Service(developer_repo)
    with app.app_context():
        country_service.fetch_gdp_data(USING_YEAR_DATA)
        click.echo("Succesfully saved GDP data, saving developer data")

        developer_service.save_from_stackoverflow()
        click.echo("Done")
