from dataclasses import dataclass, field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..country import Country


@dataclass
class Developer:
    id: int = field(init=False)
    worked_with: list[str]
    country: "Country"
    country_id: int = field(init=False)
    age_range: str
    # TODO implement has_worked_with method
