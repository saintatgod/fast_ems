from fastapi import APIRouter
from .users import users_router

api_router = APIRouter()

api_router.include_router(users_router, prefix="/users", tags=["users"])
