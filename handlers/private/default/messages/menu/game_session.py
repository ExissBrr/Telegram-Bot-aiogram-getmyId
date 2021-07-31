from aiogram.types import Message

from keyboards import inline
from loader import dp


@dp.message_handler(text='Play clicker')
async def response(message: Message):
    await message.answer(
        text='Click count: 0',
        reply_markup=inline.default.clicker.make_keyboard(count=1)
    )
