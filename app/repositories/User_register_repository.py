from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext
class UserRegistrationManager():
    def __init__(self, email: str, password: str, nickname: str,role_id: int):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.role_id = role_id

    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def hash(password: str):
        return pwd_context.hash(password)

    def verify(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    async def create_user(user: UserCreate):
        try:

            user.password = utils.hash(user.password)
            return new_user
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="already registered")