from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.app.core import settings, register_routers, reset_api_docs, lifespan

def create_app()->FastAPI:
    fastapi_app = FastAPI(**settings.get_backend_app_attributes, lifespan=lifespan)
    fastapi_app.mount(settings.STATIC_URL, app=StaticFiles(directory=settings.STATIC_ROOT))
    reset_api_docs()
    register_routers(fastapi_app)
    return fastapi_app