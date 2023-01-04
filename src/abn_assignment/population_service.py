from typing import Self
from sqlalchemy.orm import scoped_session

from abn_assignment.domain.country.service import CountryService
from abn_assignment.domain.developer.service import DeveloperService
from .constants import USING_YEAR_DATA


class PopulationService:
    __session: scoped_session
    __from_year: int

    def __init__(
        self, session: scoped_session, from_year: int = USING_YEAR_DATA
    ) -> None:
        self.__session = session
        self.__from_year = from_year

    def populate_gdp_data(self: Self):
        country_service = CountryService(self.__session)
        country_service.fetch_gdp_data(self.__from_year)

    def populate_stackoverflow_data(
        self: Self, filename: str = "survey_results_public.csv"
    ):
        developer_service = DeveloperService(self.__session)
        developer_service.save_from_stackoverflow(filename)
