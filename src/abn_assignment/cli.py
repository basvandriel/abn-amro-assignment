import click
import requests

from .constants import GDP_API_URL, USING_YEAR_DATA
from abn_assignment.domain.country import Country


@click.command()
def populate():
    """
    Program that populates a SQL database with GDP and StackOverflow from 2021.
    """
    click.echo(f"Fetching GDP data from {USING_YEAR_DATA}")

    response = requests.get(GDP_API_URL)
    json = response.json()

    dimension_geo = json["dimension"]["geo"]
    dimension_category = dimension_geo["category"]

    gdp_values = json["value"]

    gdp_indexes = dimension_category["index"]

    countries: list[Country] = [
        Country(name, iso_code)
        for iso_code, name in dimension_category["label"].items()
    ]

    for country in countries:
        try:
            gdp_index = str(gdp_indexes[country.iso_code])
            country.gdp_in_euro = gdp_values[gdp_index]
        except KeyError:
            # Some countries don't have data
            country.gdp_in_euro = None

    print(countries)
