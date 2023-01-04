from dataclasses import dataclass, field

from abn_assignment.domain.developer import Developer


@dataclass
class Country:
    id: int = field(init=False)
    name: str
    iso_code: str

    # Later intialized because of data mapping
    gdp_in_euro: float | None
    developers: list[Developer] = field(default_factory=list)
