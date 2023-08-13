from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.schemas.token_paylaod_schema import TokenData
from fastapi import Depends, status, HTTPException

from app.repositories.Db_model_definer import UsersRepository



class UserManagerRepository():
    oauth2_scheme = None  # fill these in another layer
    Model = None
    SECRET_KEY = None
    ALGORITHM = None
    ACCESS_TOKEN_EXPIRE_MINUTES = None
    async def create_acces_token(self,data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt


    async def verify_access_token(self,token: str, credentials_exception):
        try:
            print(token)
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            id: str = payload.get("user_id")
            role_id: str = payload.get("role_id")
            if id is None:
                raise credentials_exception
            token_data = TokenData(id=id, role_id= role_id)
        except JWTError:
            raise credentials_exception
        return token_data


    async def get_current_user(self,token: str = Depends(oauth2_scheme)):

        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f'Could not validate credentials',
                                          headers={"WWW-Authenticate": "Bearer"})
        token_verified = await self.verify_access_token(token, credentials_exception)
        db_manager = UsersRepository()
        user = await db_manager.find_one(id=token_verified.id)

        return user

