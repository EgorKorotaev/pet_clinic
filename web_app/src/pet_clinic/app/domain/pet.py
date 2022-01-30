import datetime
from dataclasses import dataclass


@dataclass
class Age:
    value: int


@dataclass
class Pet:
    id: str
    name: str
    data_created: datetime.date
