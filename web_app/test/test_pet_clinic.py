import os

from fastapi.testclient import TestClient
from requests import Response

from pet_clinic.app.app import app
from pet_clinic.app.storage import DB_PATH, set_db_path
from test_table import create_test_table

client = TestClient(app)


def test_register_pet():  # e2e (end to end) test
    set_db_path(os.path.join(__file__, "..", "test_db.db"))
    create_test_table()

    response: Response = client.post("/register_pet", json={"name": "Foo"})

    assert response.status_code == 201
    assert response.json()["pet_id"] is not None
    assert isinstance(response.json()["pet_id"], str)


def test_create_directive():  #
    set_db_path(os.path.join(__file__, "..", "test_db.db"))
    create_test_table()

    response: Response = client.post(
        "/create_directive", json={"title": "Bar", "cost": "100"}
    )

    assert response.status_code == 201
    assert response.json()["directive_id"] is not None
    assert isinstance(response.json()["directive_id"], str)


# def test_first_writing_doctor_directive():
#     # given
#     set_db_path(os.path.join(__file__, "..", "test_db.db"))
#     create_test_table()
#
#     register_pet_response: Response = client.post("/register_pet", json={"name": "Foo"})
#     pet_id = register_pet_response.json()["pet_id"]
#
#     create_directive_response: Response = client.post("/create_directive", json={"title": "Bar", "cost": "100"})
#     directive_id = create_directive_response.json()["directive_id"]
#
#     # when
#     response: Response = client.put("/writing_doctor_directive", data={"pet_id": pet_id, "directive_id": directive_id})
#
#     # then
#     assert response.status_code == 201
#     assert response.json()["pet_directives_id"] is not None
#     assert isinstance(response.json()["pet_directives_id"], str)


# def test_no_first_writing_doctor_directive():
#     # given
#     set_db_path(os.path.join(__file__, "..", "test_db.db"))
#     create_test_table()
#
#     register_pet_response: Response = client.post("/register_pet", json={"name": "Foo"})
#     pet_id = register_pet_response.json()["pet_id"]
#
#     create_directive_response: Response = client.post("/create_directive", json={"title": "Bar", "cost": "100"})
#     directive_id = create_directive_response.json()["directive_id"]
#
#     client.put("/writing_doctor_directive", data={"pet_id": pet_id, "directive_id": directive_id})
#
#     # when
#     response: Response = client.put(
#         "/writing_doctor_directive",
#         data={"pet_id": pet_id, "directive_id": directive_id}
#     )
#
#     # then
#     assert response.status_code == 200
#     assert response.json()["pet_directives_id"] is not None
#     assert isinstance(response.json()["pet_directives_id"], str)


def test_bill_client_for_visit():  # выставить счёт за посещение
    # given
    visit_id = 'foo'

    # when
    response: Response = client.get(f"/visit/{visit_id}/bill")

    # then
    # хочу получить "сколько стоит посещение"
    # хочу получить "список {id услуг в бух.системе ИЛИ цена, описание}"
    # service: {type: "accounting_system", value: {id_in_accounting_system: "24dw87-ds4-7410-4d5w47"}}
    # service: {type: "custom", value: {cost: "10000", description: "лечение Беременности на почве алкоголизма"}}
