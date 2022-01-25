import sqlite3
from sqlite3 import Connection

from pet_clinic.app.domain.pet import Pet
from pet_clinic.app.storage import get_db_path
from pet_clinic.app.usecase.register_pet import PetPersister


class PetRepository(PetPersister):
    def __init__(self, db: Connection):
        self.db = db

    def save_pet(self, pet: Pet) -> None:
        sql = "INSERT INTO pets (id, name, data_created) values(?, ?, ?)"
        data = (pet.id, pet.name, pet.data_created)
        self.db.execute(sql, data)


def get_pet_repository() -> PetRepository:
    return PetRepository(sqlite3.connect(get_db_path()))
