from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from keyboard import keyboard1
from aiogram import Bot, Dispatcher

from database import add_new_user,check_user, update_referals

import os
media = os.path.join(os.path.dirname(os.path.abspath(__file__)),"images")

router = Router()
bot = Bot(token="YOUR_BOT_TOKEN")

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    photo = FSInputFile(os.path.join(media, "icon1.jpg"))
    await state.clear()
    if check_user(message.chat.id) is None:
        if len(message.text[7:]) > 0:
            await bot.send_message(message.text[7:],text="Пользователь перешел по реферальной ссылке")
            update_referals(message.text[7:],1)
        add_new_user(message.chat.id,message.from_user.username,message.from_user.full_name)
    await message.answer_photo(photo=photo,
        caption=f"""👋 Привет! {message.from_user.full_name}

Все время смотрел обычный хентай?🤨

Теперь же ты можешь генерировать хентай по своему запросу😧

В день выдается по 20 запросов
Вы можете купить премиум✨ и генерировать без ограничений😦

Жми кнопку генерировать!🔥""",
        reply_markup=keyboard1()
    )

