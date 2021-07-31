from aiogram.types import Message

from data import text
from filters.messages.forwarded import Forwarded
from loader import dp


@dp.message_handler(Forwarded())
async def response(message: Message):
    await message.answer(
        text=text.message.default.answer_forward_simple.format(
            user_id=message.forward_from.id
        )
    )
