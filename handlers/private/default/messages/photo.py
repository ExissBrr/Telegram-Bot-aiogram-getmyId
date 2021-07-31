from aiogram.types import Message, ContentType

from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def response(message: Message):
    base_photo = message.photo[-1]
    await message.answer_photo(
        caption=base_photo.file_id,
        photo=base_photo.file_id
    )
