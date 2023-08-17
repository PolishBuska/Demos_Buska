from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.config import settings
from app.repositories.User_manager_repository import UserManagerRepository
from app.repositories.User_register_repository import UserRegistrationRepository
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.repositories.pwd_contex_repository import Pwd_context
from app.repositories.User_manager_repository import AuthCredValidator
class UserAuthService(UserManagerRepository):
    SECRET_KEY = settings.secret_key
    ALGORITHM = settings.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
    Model = User
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
    auth_validator = AuthCredValidator()



class UserRegService(UserRegistrationRepository):
    __pwd_context__ = Pwd_context.__pwd_context__