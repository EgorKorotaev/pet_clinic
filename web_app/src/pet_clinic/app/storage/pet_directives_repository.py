import sqlite3
from sqlite3 import Connection

from pet_clinic.app.domain.directive import Directive
from pet_clinic.app.domain.pet_directives import PetDirectives
from pet_clinic.app.storage import get_db_path
from pet_clinic.app.usecase.writing_doctor_directive import PetDirectivesPersister


class PetDirectivesRepository(PetDirectivesPersister):
    def __init__(self, db: Connection):
        self.db = db

    def is_there_pet_directive(self, pet_directives: PetDirectives) -> bool:
        pass

    def create_pet_directive(self, pet_directives: PetDirectives) -> None:
        pass

    def add_pet_directive(self, pet_directives: PetDirectives) -> None:
        pass

    # def save_directive(self, directive: Directive) -> None:
    #     sql = "INSERT INTO directives (id, title, cost) values(?, ?, ?)"
    #     data = (directive.id, directive.title, directive.cost)
    #     self.db.execute(sql, data)


def get_pet_directives_repository() -> PetDirectivesRepository:
    return PetDirectivesRepository(sqlite3.connect(get_db_path()))
