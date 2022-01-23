from fastapi import APIRouter
from starlette.responses import FileResponse

from app.api.routes import doctor, owner, site

router = APIRouter()
router.include_router(doctor.router, tags=["doctor"], prefix="/doctor")
router.include_router(owner.router, tags=["owner"], prefix="/owner")
router.include_router(site.router, tags=["site"], prefix="/site")


@router.get('/favicon.ico')
def favicon():
    return FileResponse('../media/favicon.ico')
