from abc import ABC, abstractmethod
from dataclasses import dataclass

from pet_clinic.app.domain.pet_directives import PetDirectives


@dataclass
class WritingDoctorDirectiveRequest:
    pet_id: str
    directive_id: str


class PetDirectivesPersister(ABC):
    @abstractmethod
    def is_there_pet_directive(self, pet_directives: PetDirectives) -> bool:
        pass

    @abstractmethod
    def create_pet_directive(self, pet_directives: PetDirectives) -> None:
        pass

    @abstractmethod
    def add_pet_directive(self, pet_directives: PetDirectives) -> None:
        pass


def is_there_pet_doctor_directive(
    writing_doctor_directive_request: WritingDoctorDirectiveRequest,
    pet_directives_persister: PetDirectivesPersister
) -> bool:
    pass


def create_writing_pet_doctor_directive(
    writing_doctor_directive_request: WritingDoctorDirectiveRequest,
    pet_directives_persister: PetDirectivesPersister,
) -> str:
    pass


def supplement_writing_pet_doctor_directive(
    writing_doctor_directive_request: WritingDoctorDirectiveRequest,
    pet_directives_persister: PetDirectivesPersister,
) -> str:
    pass
