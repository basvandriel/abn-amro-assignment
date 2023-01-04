from typing import Self
from abn_assignment.domain.country import Country
import requests


class CountryFetcher:
    def __resolve_gdp_api_url(self: Self, year: int) -> str:
        # Neighboring string constants are automatically concatenated
        # https://stackoverflow.com/a/1874679/2989034
        return (
            "https://ec.europa.eu/eurostat/api/dissemination/statistics"
            "/1.0/data/TEC00001"
            f"?format=JSON&lang=en&unit=CP_EUR_HAB&time={year}"
        )

    def fetch(self: Self, year: int) -> list[Country]:
        response = requests.get(self.__resolve_gdp_api_url(year))
        json = response.json()

        dimension_geo = json["dimension"]["geo"]
        dimension_category = dimension_geo["category"]

        gdp_values: dict[str, float] = json["value"]
        gdp_indexes = dimension_category["index"]
        labels = dimension_category["label"].items()

        # .get returns None if key can't be found
        countries = [
            Country(name, iso, gdp_values.get(str(gdp_indexes.get(iso))))
            for iso, name in labels
        ]
        return countries
