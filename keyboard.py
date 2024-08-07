from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types




def keyboard1():
    
    row1=[

        [
        types.KeyboardButton(text="Генерация🤖")
        ],
        [types.KeyboardButton(text="Готовые фото💾")],
        [
        types.KeyboardButton(text="Профиль👤")

        ]

    ]


    row = types.ReplyKeyboardMarkup(
        keyboard=row1,
        resize_keyboard=True,
        input_field_placeholder="Жми!"
        )

    return row



def keyboard2():
    
    row1=[

        [
        types.KeyboardButton(text="Аниме🖊"),
        types.KeyboardButton(text="Порно👩‍🦰"),
        types.KeyboardButton(text="Фурри😽"),
        ],
        [
        types.KeyboardButton(text="Главное меню🏡")

        ]

    ]


    row = types.ReplyKeyboardMarkup(
        keyboard=row1,
        resize_keyboard=True,
        input_field_placeholder="Жми!"
        )

    return row





def add_wallet_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Привязать кошелек",callback_data="add_wallet")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
