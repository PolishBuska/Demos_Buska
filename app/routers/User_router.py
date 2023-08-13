from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.User_auth_service import UserRegService


router = APIRouter(
    prefix='/user',
    tags=['songs']
)


@router.post('/user/create')
async def register_user(user: UserCreate):
    user_manager = UserRegService()
    user = await user_manager.create_user(user)
    return user
