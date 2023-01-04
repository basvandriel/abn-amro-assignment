from abn_assignment.domain.country import Country
from abn_assignment.domain.developer.constants import (
    STACKOVERFLOW_INSIGHTS_COUNTRY_INDEX,
    STACKOVERFLOW_INSIGHTS_WORKED_WITH_INDEX,
    STACKOVERFLOW_INSIGHTS_YEAR_1ST_CODE_INDEX,
)
from sqlalchemy.orm import scoped_session, Query

from . import Developer
from typing import Self

import csv

from abn_assignment.constants import DATA_DIR


class Service:
    __session: scoped_session

    def __init__(self: Self, session: scoped_session) -> None:
        self.__session = session

    def save_from_stackoverflow(
        self: Self, filename: str = "survey_results_public.csv"
    ) -> list[Developer]:
        devs: list[Developer] = []

        with open(DATA_DIR / filename) as f:
            reader = csv.reader(f)

            # The line will skip the first row of the csv file (Header row)
            next(reader)

            for row in reader:
                country_query: Query = self.__session.query(Country).filter_by(
                    name=row[STACKOVERFLOW_INSIGHTS_COUNTRY_INDEX]
                )
                country: Country | None = country_query.first()

                if not country:
                    # TODO throw error here
                    continue

                worked_with_unformatted: str = row[
                    STACKOVERFLOW_INSIGHTS_WORKED_WITH_INDEX
                ]
                worked_with: list[str] = worked_with_unformatted.split(";")
                firstcode = row[STACKOVERFLOW_INSIGHTS_YEAR_1ST_CODE_INDEX]

                dev = Developer(worked_with, country, firstcode)
                devs.append(dev)

        return devs
