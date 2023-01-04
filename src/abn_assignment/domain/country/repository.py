from abc import ABC, abstractmethod
from typing import Self

from abn_assignment.domain.country import Country


class CountryRepository(ABC):
    @abstractmethod
    def get_by_iso_code(self: Self, iso_code: str) -> Country | None:
        ...

    @abstractmethod
    def get_by_name(self: Self, country_name: str) -> Country | None:
        ...

    @abstractmethod
    def save_list(self: Self, entities: list[Country]):
        ...
