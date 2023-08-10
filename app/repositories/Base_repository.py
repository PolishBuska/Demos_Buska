from abc import ABC,abstractmethod

class BaseAbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError
    @abstractmethod
    async def find_one(self):
        raise NotImplementedError

