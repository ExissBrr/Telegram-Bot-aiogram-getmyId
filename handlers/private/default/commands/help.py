from aiogram.dispatcher.filters import CommandHelp
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandHelp())
async def response(message: Message):
    await message.answer(
        text='help'
    )