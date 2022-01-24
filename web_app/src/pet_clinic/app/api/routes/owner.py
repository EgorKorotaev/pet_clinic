from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
import sqlite3 as sl

router = APIRouter()


@router.get("/come")
async def come(
        species: str,
        name: str
):
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
    )
    if species is None or name is None:
        return wrong_login_error

    bd = sl.connect('pet_clinic.db')

    sql = 'INSERT INTO PETS (id, species, name, owner, status, diagnosis, doctor) values(NULL, ?, ?, ?, ?, ?, ?)'
    data = [(species, name, 'Owner', 'поступил', 'NULL', "NULL")]
    with bd:
        bd.executemany(sql, data)

    _row = []
    with bd:
        data = bd.execute("SELECT * FROM PETS WHERE species = ? AND name = ?", (species, name))
        for row in data:
            print(row)
            _row.append(row)

    return {"message": _row}


@router.get("/visit")
async def come(
        species: str,
        name: str
):
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
    )
    if species is None or name is None:
        return wrong_login_error

    bd = sl.connect('pet_clinic.db')

    _row = []
    with bd:
        data = bd.execute("SELECT * FROM PETS WHERE species = ? AND name = ?", (species, name))
        for row in data:
            print(row)
            _row.append(row)

    return {"message": _row}
