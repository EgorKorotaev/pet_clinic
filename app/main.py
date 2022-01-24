from fastapi import FastAPI
from starlette.responses import FileResponse

from app import bd
from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(api_router)

    return application


app = get_application()
