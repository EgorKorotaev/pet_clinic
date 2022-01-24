from fastapi import APIRouter
from starlette.responses import FileResponse
import sqlite3 as sl

from pet_clinic.app.api.routes import doctor
from pet_clinic.app.api.routes import owner
from pet_clinic.app.api.routes import site

router = APIRouter()
router.include_router(doctor.router, tags=["doctor"], prefix="/doctor")
router.include_router(owner.router, tags=["owner"], prefix="/owner")
router.include_router(site.router, tags=["site"], prefix="/site")


@router.get("/bd")
async def bd():
    bd = sl.connect('pet_clinic.db')

    output = {}
    with bd:
        data = bd.execute("SELECT * FROM PETS")
        for row in data:
            print(row)
            output[row[0]] = row

    return output