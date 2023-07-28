from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:' \
                          f'{settings.database_password}@' \
                          f'{settings.database_hostname}:' \
                          f'{settings.database_port}/' \
                          f'{settings.database_name}'


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session