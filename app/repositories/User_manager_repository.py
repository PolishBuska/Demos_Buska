from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

from app.config import settings
from app.db import async_session_maker
from app.models.user_model import User
from app.schemas.token_paylaod_schema import TokenData
from fastapi import Depends, status, HTTPException
from sqlalchemy import select
from app.repositories.Db_model_definer import UsersRepository
from app.repositories.SQLAlchemy_repository import SQLAlchemyRepository
from app.repositories.pwd_contex_repository import Pwd_context

class UserManagerRepository():
    SECRET_KEY = settings.secret_key
    ALGORITHM = settings.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
    Model = User
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
    async def create_acces_token(self,data: dict):
        if not isinstance(data, dict):
            raise ValueError("Invalid input data")
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt


    async def verify_access_token(self,token: str, credentials_exception):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            id =  payload.get("user_id")
            print(id)
            role_id =  payload.get("user_role_id")
            print(role_id)
            if id is None:
                raise credentials_exception
            token_data = TokenData(id=id, role_id= role_id)
        except JWTError:
            raise credentials_exception
        return token_data
    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        try:
            credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f'Could not validate credentials',
                                          headers={"WWW-Authenticate": "Bearer"})
            token_verified = await self.verify_access_token(token, credentials_exception)
            db_manager = UsersRepository()
            user = await db_manager.find_one(id=token_verified.id)
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f'Could not validate credentials',
                                          headers={"WWW-Authenticate": "Bearer"})
        return user

class AuthCredValidator(SQLAlchemyRepository):
    pwd_context = Pwd_context.__pwd_context__
    model = User
    async def validate(self, email: str,plain_password: str):
        async with async_session_maker() as session:
            query_user = select(self.model).where(self.model.email == email)
            res = await session.execute(query_user)
            res_out = res.scalar()
            if not self.pwd_context.verify(plain_password, res_out.password):
                raise HTTPException(status.HTTP_403_FORBIDDEN,detail="Wrong credentials")
            return res_out




