from . import Developer
from typing import Self


class Service:
    def save_from_stackoverflow(self: Self) -> list[Developer]:
        ...
