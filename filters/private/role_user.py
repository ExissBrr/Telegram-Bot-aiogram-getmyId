from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from utils.db_api.models.user import DBCommands


class NewUser(BoundFilter):
    async def check(self, message: Message):
        user_id = message.from_user.id
        return not await DBCommands.is_user(id=user_id)
