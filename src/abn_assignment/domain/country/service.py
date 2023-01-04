from typing import Self
from sqlalchemy.orm import scoped_session
from abn_assignment.domain.country import Country

from abn_assignment.domain.country.fetcher import CountryFetcher
from abn_assignment.domain.developer import Developer
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
        query = self.__session.query(Country).filter_by(iso_code=iso_code)
        country: Country | None = query.first()

        if not country:
            raise Exception("ISO-code not found")

        # manual order from here
        # https://insights.stackoverflow.com/survey/2021#section-experience-writing-that-first-line-of-code
        youngest_dev: Developer | None = (
            self.__session.query(Developer)
            .filter_by(country_id=country.id)
            .order_by(Developer.age_range)
            .first()
        )
        if not youngest_dev:
            raise Exception("Developer not found")

        # TODO create repo
        # create query to find by iso code
        # if none return errors
        return YoungestCodingGDP(country.gdp_in_euro, youngest_dev.age_range)
