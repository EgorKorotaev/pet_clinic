import datetime
from dataclasses import dataclass


@dataclass
class Directive:
    id: str
    title: str
    cost: str
