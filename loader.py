from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from data.config import TOKEN_BOT
from gino import Gino

database = Gino()
storage = MemoryStorage()
bot = Bot(
    token=TOKEN_BOT,
    parse_mode=ParseMode.HTML
)
dp = Dispatcher(
    bot=bot,
    storage=storage
)
__all__ = ['dp', 'bot', 'storage', 'database']
