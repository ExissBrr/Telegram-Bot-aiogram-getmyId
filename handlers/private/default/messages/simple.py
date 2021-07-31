from aiogram.types import Message

import data
from loader import dp


@dp.message_handler()
async def response(message: Message):
    await message.answer(
        text=data.text.message.default.answer_simple_message.format(
            user_id=message.from_user.id
        )
    )
