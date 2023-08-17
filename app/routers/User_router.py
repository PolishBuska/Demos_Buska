from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import UserOut
from app.schemas.user_schema import UserCreate
from app.schemas.token_schema import Token
from app.services.User_auth_service import UserRegService

from app.services.User_auth_service import UserAuthService

router = APIRouter(
    tags=['songs']
)


@router.post('/user/create',response_model=UserOut)
async def register_user(user: UserCreate):
    user_manager = UserRegService()
    user_result = await user_manager.create_user(user)
    return user_result


@router.post('/login', response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user_auth_manager = UserAuthService()
    validator = user_auth_manager.auth_validator
    user = await validator.validate(email=user_credentials.username,
                                                     plain_password=user_credentials.password)

    access_token = await user_auth_manager.create_acces_token(data={"user_id": user.id,
                                                             "user_role_id": user.role_id})

    return {"access_token": access_token, "token_type": "bearer"}

