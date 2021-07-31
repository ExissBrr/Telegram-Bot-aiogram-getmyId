from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class Forwarded(BoundFilter):
    async def check(self, message: Message):
        return message.forward_from
