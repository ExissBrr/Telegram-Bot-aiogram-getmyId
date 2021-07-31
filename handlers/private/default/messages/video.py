from aiogram.types import ContentType, Message

from loader import dp


@dp.message_handler(content_types=ContentType.VIDEO)
async def response(message: Message):
    await message.answer_video(
        video=message.video.file_id,
        caption=message.video.file_id
    )
