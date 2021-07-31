from aiogram import Dispatcher

from utils.db_api.database import Database
from utils.misc.set_bot_commands import set_commands


async def on_startup(dispatcher: Dispatcher):
    await set_commands(dispatcher)
    await Database.create_bind()
    await Database.create_tables()
    print("Bot is start polling..")
