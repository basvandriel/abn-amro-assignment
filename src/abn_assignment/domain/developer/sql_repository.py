from typing import Self
from abn_assignment.domain.country import Country
from abn_assignment.domain.developer import Developer
from .repository import DeveloperRepository
from sqlalchemy.orm import scoped_session


class SQLDeveloperRepository(DeveloperRepository):
    __session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.__session = session

    def get_youngest_by_country(
        self: Self,
        country: Country,
    ) -> Developer | None:
        youngest_dev: Developer | None = (
            self.__session.query(Developer)
            .filter_by(country_id=country.id)
            .order_by(Developer.age_range)
            .first()
        )
        return youngest_dev
