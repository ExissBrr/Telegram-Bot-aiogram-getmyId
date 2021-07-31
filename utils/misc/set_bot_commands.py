from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

commands = {
    "/start": "Start session",
    "/help": "Get help",
    "/settings": "Your private settings"
}


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        commands=[
            BotCommand(command=com, description=des) for com, des in commands.items()
        ]

    )
