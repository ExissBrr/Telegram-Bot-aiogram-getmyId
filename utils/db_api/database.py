from data.config import PG_URL
from loader import database


class Database:
    @staticmethod
    async def create_bind():
        await database.set_bind(bind=PG_URL)

    @staticmethod
    def pop_bind():
        database.pop_bind()

    @staticmethod
    async def create_tables():
        await database.gino.create_all()
        print("Создана таблица")

    @staticmethod
    async def drop_tables():
        await database.gino.drop_all()
