import os

from fastapi.testclient import TestClient
from requests import Response

from pet_clinic.app.app import app
from pet_clinic.app.storage import DB_PATH, set_db_path
from test_pet_repository import create_test_table

client = TestClient(app)


def test_register_pet():  # e2e (end to end) test
    set_db_path(os.path.join(__file__, "..", "test_db.db"))
    create_test_table()

    response: Response = client.post("/register_pet", json={"name": "Foo"})

    assert response.status_code == 201
    # assert response.json().keys() == ["pet_id"]
    assert response.json()["pet_id"] is not None
    assert isinstance(response.json()["pet_id"], str)
