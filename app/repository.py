from abc import ABC,abstractmethod

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError




class SQLAlchemyRepository(AbstractRepository,):
    model = None
    async def add_one(self,data: dict):
        async with async_sessionmaker as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute()
            return res.scalar_one()

    async def find_all(self):
        pass