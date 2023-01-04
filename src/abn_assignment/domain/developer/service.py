from abn_assignment.domain.country.repository import CountryRepository
from abn_assignment.domain.developer.constants import (
    STACKOVERFLOW_INSIGHTS_COUNTRY_INDEX,
    STACKOVERFLOW_INSIGHTS_WORKED_WITH_INDEX,
    STACKOVERFLOW_INSIGHTS_YEAR_1ST_CODE_INDEX,
)
from abn_assignment.domain.developer.repository import DeveloperRepository

from . import Developer
from typing import Self

import csv

from abn_assignment.constants import DATA_DIR


class Service:
    __developer_repo: DeveloperRepository
    __country_repo = CountryRepository

    def __init__(
        self: Self,
        developer_repo: DeveloperRepository,
        country_repo: CountryRepository,
    ) -> None:
        self.__developer_repo = developer_repo
        self.__country_repo = country_repo

    def save_from_stackoverflow(
        self: Self, filename: str = "survey_results_public.csv"
    ) -> list[Developer]:
        devs: list[Developer] = []

        with open(DATA_DIR / filename) as f:
            reader = csv.reader(f)

            # The line will skip the first row of the csv file (Header row)
            next(reader)

            for row in reader:
                country = self.__country_repo.get_by_name(
                    row[STACKOVERFLOW_INSIGHTS_COUNTRY_INDEX]
                )

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

        self.__developer_repo.save_list(devs)

        return devs
