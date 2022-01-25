import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4

from pet_clinic.app.domain.pet import Pet, Age


@dataclass
class RegisterPetRequest:
    name: str
    # age: Age


class PetPersister(ABC):
    @abstractmethod
    def save_pet(self, pet: Pet) -> None:
        pass


def register_pet(
    register_pet_request: RegisterPetRequest, pet_persister: PetPersister
) -> str:
    pet_id = str(uuid4())
    pet = Pet(
        id=pet_id, name=register_pet_request.name, data_created=datetime.date.today()
    )
    pet_persister.save_pet(pet)
    return pet_id
