from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import sqlite3 as sl

from pet_clinic.app.api.routes import doctor
from pet_clinic.app.api.routes import owner
from pet_clinic.app.api.routes import site
from pet_clinic.app.storage.directive_repository import get_directive_repository
from pet_clinic.app.storage.pet_directives_repository import get_pet_directives_repository
from pet_clinic.app.storage.pet_repository import get_pet_repository
from pet_clinic.app.usecase.create_directive import (
    create_directive,
    CreateDirectiveRequest,
)
from pet_clinic.app.usecase.register_pet import register_pet, RegisterPetRequest
from pet_clinic.app.usecase.writing_doctor_directive import WritingDoctorDirectiveRequest, \
    is_there_pet_doctor_directive, create_writing_pet_doctor_directive, supplement_writing_pet_doctor_directive

router = APIRouter()
router.include_router(doctor.router, tags=["doctor"], prefix="/doctor")
router.include_router(owner.router, tags=["owner"], prefix="/owner")
router.include_router(site.router, tags=["site"], prefix="/site")


class PetRequest(BaseModel):
    name: str


class DirectiveRequest(BaseModel):
    title: str
    cost: str


class DoctorDirectiveRequest(BaseModel):
    pet_id: str
    directive_id: str


@router.post("/register_pet", status_code=201)
def register_pet_handler(request: PetRequest):
    pet_id = register_pet(
        RegisterPetRequest(request.name),
        get_pet_repository()
    )
    return {"pet_id": pet_id}


@router.post("/create_directive", status_code=201)
def create_directive_handler(request: DirectiveRequest):
    directive_id = create_directive(
        CreateDirectiveRequest(request.title, request.cost),
        get_directive_repository()
    )
    return {"directive_id": directive_id}


@router.post("/writing_doctor_directive")
def writing_doctor_directive_handler(request: DoctorDirectiveRequest):
    writing_doctor_directive_request = WritingDoctorDirectiveRequest(
        request.pet_id,
        request.directive_id
    )
    pet_directives_repository = get_pet_directives_repository()
    if is_there_pet_doctor_directive(writing_doctor_directive_request, pet_directives_repository):
        response = create_writing_pet_doctor_directive(writing_doctor_directive_request, pet_directives_repository)
        return Response(status_code=201, content=response)
    else:
        response = supplement_writing_pet_doctor_directive(writing_doctor_directive_request, pet_directives_repository)
        return Response(status_code=200, content=response)
