from dataclasses import dataclass, field


@dataclass
class Country:
    id: int = field(init=False)
    name: str
    iso_code: str
    gdp_in_euro: float
