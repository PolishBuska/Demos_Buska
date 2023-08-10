
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.repositories.Base_repository import BaseAbstractRepository

class SQLAlchemyRepository(BaseAbstractRepository):
    model = None
    async def add_one(self, data: dict) -> int:
        async with async_sessionmaker as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute()
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_sessionmaker as session:
            query = select(self.model)
            res = await session.execute(query)
            [row[0].to_read_model() for row in res.all()]
            return res.scalar_one()

    async def find_one(self, id: int):
        async with async_sessionmaker as session:
            query = select(self.model).where(self.model.id == id).scalar_one()
            res = await session.execute(query)
            return res.scalar_one()
