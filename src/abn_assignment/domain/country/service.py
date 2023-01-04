from typing import Self
from abn_assignment.domain.country import Country

from abn_assignment.domain.country.fetcher import CountryFetcher
from abn_assignment.domain.country.repository import CountryRepository
from abn_assignment.domain.developer.repository import DeveloperRepository
from abn_assignment.domain.youngest_gdp_response import YoungestCodingGDP


class CountryService:
    __country_repo: CountryRepository
    __developer_repo: DeveloperRepository

    def __init__(
        self,
        country_repo: CountryRepository,
        developer_repo: DeveloperRepository,
    ) -> None:
        self.__country_repo = country_repo
        self.__developer_repo = developer_repo

    def fetch_gdp_data(self: Self, year: int):
        countries: list[Country] = CountryFetcher().fetch(year)
        self.__country_repo.save_list(countries)

    def get_youngest_gdp(self: Self, iso_code: str) -> YoungestCodingGDP:
        country = self.__country_repo.get_by_iso_code(iso_code)

        if not country:
            raise ValueError("ISO-code not found")

        if dev := (self.__developer_repo.get_youngest_by_country(country)):
            return YoungestCodingGDP(country.gdp_in_euro, dev.age_range)
        else:
            raise ValueError("Developer not found")
