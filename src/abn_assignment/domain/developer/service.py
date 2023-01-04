from . import Developer
from typing import Self

import csv

from abn_assignment.constants import DATA_DIR


class Service:
    def save_from_stackoverflow(
        self: Self, filename: str = "survey_results_public.csv"
    ) -> list[Developer]:
        devs: list[Developer] = []

        with open(DATA_DIR / filename) as f:
            reader = csv.reader(f)
            for row in reader:
                country_name: str = row[3]
                worked_with_unformatted: str = row[16]
                worked_with: list[str] = worked_with_unformatted.split(";")

                year_first_code = row[7]

                # Developer(worked_with)
                print(row)

        return devs
