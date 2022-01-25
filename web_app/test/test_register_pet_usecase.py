import datetime
from dataclasses import dataclass

from pet_clinic.app.domain.pet import Pet
from pet_clinic.app.usecase.register_pet import (
    RegisterPetRequest,
    Age,
    register_pet,
    PetPersister,
)


@dataclass
class TestStorage(PetPersister):
    pet: Pet | None = None

    def save_pet(self, pet: Pet) -> None:
        self.pet = pet

    def get_result(self) -> Pet:
        return self.pet


def test_pet_is_registered():  # unit test
    # given
    pet_name = "name"
    register_pet_request = RegisterPetRequest(pet_name)
    test_storage = TestStorage()

    # when
    pet_id = register_pet(register_pet_request, test_storage)

    # then
    pet_expected = Pet(id=pet_id, name=pet_name, data_created=datetime.date.today())
    pet_actual = test_storage.get_result()
    assert pet_expected == pet_actual
    # assert pet_expected.age == pet_actual.age
