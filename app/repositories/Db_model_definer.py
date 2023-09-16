from app.repositories.SQLAlchemy_repository import SQLAlchemyRepository
from app.models.song_model import Songs

from app.models.user_model import User


class SongsRepository(SQLAlchemyRepository):
    model = Songs


class UsersRepository(SQLAlchemyRepository):
    model = User


