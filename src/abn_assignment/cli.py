import click
from abn_assignment.population_service import PopulationService

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

    service = PopulationService(database.session)

    with app.app_context():
        service.populate_gdp_data()
        click.echo("Succesfully saved GDP data, saving developer data")

        service.populate_stackoverflow_data()
        click.echo("Done")
