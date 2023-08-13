from fastapi import Depends
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_session, AsyncSession
from app.repositories.Base_repository import BaseAbstractRepository
from app.db import get_async_session
class SQLAlchemyRepository(BaseAbstractRepository):
    model = None
    async def add_one(self, data: dict,) -> int:
            session = get_async_session()
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.
            return res.scalar_one()

    async def find_all(self):
        with async_session as session:
            query = select(self.model)
            res = await session.execute(query)
            [row[0].to_read_model() for row in res.all()]
            return res.scalar_one()

    async def find_one(self, id: int):
        async with async_session as session:
            query = select(self.model).where(self.model.id == id).scalar_one()
            res = await session.execute(query)
            return res.scalar_one()
