from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/users")
async def get_users():
    return {"users": "这是一个测试数据"}