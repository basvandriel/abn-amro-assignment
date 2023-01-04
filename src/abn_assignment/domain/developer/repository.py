from abc import ABC, abstractmethod
from typing import Self
from abn_assignment.domain.country import Country

from abn_assignment.domain.developer import Developer


class DeveloperRepository(ABC):
    @abstractmethod
    def get_youngest_by_country(
        self: Self, country: Country
    ) -> Developer | None:  # flake8: ignore E501
        ...

    @abstractmethod
    def save_list(self: Self, entities: list[Developer]):
        ...
