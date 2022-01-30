import datetime
from dataclasses import dataclass


@dataclass
class PetDirectives:
    id: str
    pet_id: str
    directives_id: list[str]
    data_created: datetime.date
