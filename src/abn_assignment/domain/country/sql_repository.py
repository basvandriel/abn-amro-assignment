from typing import Self
from abn_assignment.domain.country import Country
from abn_assignment.domain.country.repository import CountryRepository
from sqlalchemy.orm import scoped_session


class SQLCountryRepository(CountryRepository):
    __session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.__session = session

    def get_by_iso_code(self: Self, iso_code: str) -> Country | None:
        query = self.__session.query(Country).filter_by(iso_code=iso_code)
        country: Country | None = query.first()

        return country

    def save_list(self: Self, entities: list[Country]):
        self.__session.add_all(entities)
        self.__session.commit()
