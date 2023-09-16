from app.repositories.User_manager_repository import UserManagerRepository
from app.repositories.User_register_repository import UserRegistrationRepository
from app.repositories.pwd_contex_repository import Pwd_context
from app.repositories.User_manager_repository import AuthCredValidator


class UserAuthService(UserManagerRepository):
    auth_validator = AuthCredValidator()


class CurrentUserGet():
    auth = UserAuthService()


class UserRegService(UserRegistrationRepository):
    __pwd_context__ = Pwd_context.__pwd_context__
