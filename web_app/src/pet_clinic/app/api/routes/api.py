from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3 as sl

from pet_clinic.app.api.routes import doctor
from pet_clinic.app.api.routes import owner
from pet_clinic.app.api.routes import site
from pet_clinic.app.storage.pet_repository import get_pet_repository
from pet_clinic.app.usecase.register_pet import register_pet, RegisterPetRequest

router = APIRouter()
router.include_router(doctor.router, tags=["doctor"], prefix="/doctor")
router.include_router(owner.router, tags=["owner"], prefix="/owner")
router.include_router(site.router, tags=["site"], prefix="/site")


@router.get("/bd")
async def bd():
    bd = sl.connect("pet_clinic.db")

    output = {}
    with bd:
        data = bd.execute("SELECT * FROM PETS")
        for row in data:
            print(row)
            output[row[0]] = row

    return output


class PetRequest(BaseModel):
    name: str


@router.post("/register_pet", status_code=201)
def register_pet_handler(request: PetRequest):
    pet_id = register_pet(RegisterPetRequest(request.name), get_pet_repository())
    return {"pet_id": pet_id}
