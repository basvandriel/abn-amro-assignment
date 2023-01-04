from typing import Self
from sqlalchemy.orm import scoped_session

from abn_assignment.domain.country.fetcher import CountryFetcher
from abn_assignment.domain.youngest_gdp_response import YoungestCodingGDP


class CountryService:
    __session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.__session = session

    def fetch_gdp_data(self: Self, year: int):
        countries = CountryFetcher().fetch(year)

        self.__session.add_all(countries)
        self.__session.commit()

    def get_youngest_gdp(self: Self, iso_code: str) -> YoungestCodingGDP:
        # TODO create repo
        # create query to find by iso code
        # if none return errors
        return YoungestCodingGDP(30.3, "nee")
