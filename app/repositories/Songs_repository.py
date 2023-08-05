from app.repositories.SQLAlchemy_repository import SQLAlchemyRepository
from app.models.song_model import Songs

class SongsRepository(SQLAlchemyRepository):
    model = Songs