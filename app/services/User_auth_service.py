from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.repositories.User_manager_repository import UserManagerRepository
from app.models.user_model import User
class UserAuthService(UserManagerRepository):
    SECRET_KEY = settings.secret_key
    ALGORITHM = settings.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
    Model = User
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
