from asyncio.tasks import sleep

from aiogram.types import CallbackQuery

from keyboards import inline
from keyboards.callback_data.default import click_counter_cd
from loader import dp


@dp.callback_query_handler(click_counter_cd.filter())
async def count_increase(call: CallbackQuery, callback_data: dict):
    count = callback_data.get('count')
    await call.answer(text=f'{count}***',cache_time=5)
    await call.message.edit_text(
        text=f'Click count: {count}',
        reply_markup=inline.default.clicker.make_keyboard(count=int(count) + 1)
    )
