from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from starlette import status
from app.schemas.user_schema import UserCreate
from app.repositories.Db_model_definer import UsersRepository


class UserRegistrationRepository():
    __pwd_context__ = None

    def __hash_password__(self, password: str):
        return self.__pwd_context__.hash(password)

    async def create_user(self, user: UserCreate):
        try:
            user.password = self.__hash_password__(user.password)
            db_manager = UsersRepository()
            await db_manager.add_one(data=user.model_dump())
            return user.to_read_model()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="already registered")