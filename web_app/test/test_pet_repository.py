import datetime

from pet_clinic.app.domain.pet import Pet
from pet_clinic.app.storage.pet_repository import PetRepository
from test_table import create_test_table


def test_save_pet():  # integration test
    # given
    pet_id = "_42"
    data_created = datetime.date(2012, 12, 24)
    pet = Pet(id=pet_id, name="bobic", data_created=data_created)
    db = create_test_table()
    pet_reposutory = PetRepository(db)

    # when
    pet_reposutory.save_pet(pet)

    # then
    sql = "SELECT id, name, data_created FROM pets WHERE id = ?"
    result = db.execute(sql, [pet_id]).fetchall()[0]
    assert result == (pet_id, pet.name, str(data_created))
