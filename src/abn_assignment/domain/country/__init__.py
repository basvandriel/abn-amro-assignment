from dataclasses import dataclass, field

from abn_assignment.developer import Developer


@dataclass
class Country:
    id: int = field(init=False)
    name: str
    iso_code: str
    gdp_in_euro: float
    developers: list[Developer] = field(default_factory=list)
