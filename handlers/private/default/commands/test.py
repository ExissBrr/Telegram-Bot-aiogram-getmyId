from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters.private.role_user import NewUser
from loader import dp
from states.default.test_states import Test


@dp.message_handler(NewUser(), Command('test'), state=None)
async def response(message: Message):
    await message.answer(
        text="Начало теста.Вы любите картофель?"
    )
    await Test.s1.set()


@dp.message_handler(state=Test.s1)
async def s1_response(message: Message, state: FSMContext):
    answer = "Спасибо за однозначность"
    await state.update_data(answer1=message.text)
    if message.text.lower() == 'да':
        answer = 'Пизда,даун'
    elif message.text.lower() == 'нет':
        answer = 'Минет,даун'
    await message.answer(
        text=f" {answer}. Следующий вопрос. Ты позер?"
    )
    await Test.s2.set()


@dp.message_handler(state=Test.s2)
async def s2_response(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    await message.answer(
        text=f"a1={answer1}, a2={answer2}"
    )
    await state.finish()
