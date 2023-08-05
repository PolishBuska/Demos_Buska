from abc import ABC,abstractmethod
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

class BaseAbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

