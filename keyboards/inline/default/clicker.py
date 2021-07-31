from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data.default import click_counter_cd


def make_keyboard(count):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Click',
                    callback_data=click_counter_cd.new(count=count)
                )
            ]
        ]
    )
    return keyboard
