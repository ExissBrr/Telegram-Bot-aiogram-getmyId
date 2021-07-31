from aiogram import Dispatcher

from utils.db_api.database import Database


async def on_shutdown(dispatcher: Dispatcher):
    await Database.drop_tables()
    Database.pop_bind()
    print("Stop pulling")
