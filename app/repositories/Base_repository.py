from abc import ABC,abstractmethod

class BaseAbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError
    @abstractmethod
    async def find_one(self, id: int):
        raise NotImplementedError

