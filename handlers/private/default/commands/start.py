from asyncio.tasks import sleep

from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from filters.private.role_user import NewUser
from keyboards import reply
from loader import dp
from utils.db_api.models.user import DBCommands


@dp.message_handler(NewUser(), CommandStart())
async def response(message: Message):
    await DBCommands.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name
    )
    await message.answer(
        text="Welcome, new user!"
    )


@dp.message_handler(CommandStart())
async def response(message: Message):
    bot_answer = await message.answer(
        text='Now you yield wield a keyboard',
        reply_markup=reply.default.start.keyboard
    )
    await sleep(5)
    await message.delete()
    await bot_answer.delete()
