from aiogram import Router, F,types,Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboard import keyboard1, keyboard2
from aiogram import html

from aiogram.utils.chat_action import ChatActionSender

import asyncio
import requests
import random

from database import add_new_user, check_user, check_balance, update_balance, update_balance_wiwod, check_wallet, update_wallet, check_referals
from links import get_anime, get_porn, get_furry

import os
media = os.path.join(os.path.dirname(os.path.abspath(__file__)),"images")

results1 = get_anime()
results2 = get_porn()
results3 = get_furry()


router = Router()
CHANNEL_ID = "YOUR_CHANEL_CHAT_ID"
bot = Bot(token="YOUR_BOT_TOKEN")




##############################
class Order(StatesGroup):
    gen = State()
    gen2 = State()






#####################################################
@router.message(F.text == "Аниме🖊")
async def hentai(message: Message, state: FSMContext):
    if check_user(message.chat.id) is None:
        add_new_user(message.chat.id,message.from_user.username,message.from_user.full_name)
        
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

    if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
        results = results1
        i = random.randint(0,len(results))
        zxc = results[i]
        asd = zxc["imageUrl"]
        await message.answer_photo(photo=asd)
    else:
        await message.answer("Подпишись на @HentaiTonBot чтобы бот мог работать!")






@router.message(F.text == "Порно👩‍🦰")
async def porno(message: Message, state: FSMContext):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

    if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
        results = results2
        i = random.randint(0,len(results))
        zxc = results[i]
        asd = zxc["imageUrl"]
        await message.answer_photo(photo=asd)
    else:
        await message.answer("Подпишись на @HentaiTonBot чтобы бот мог работать!")








@router.message(F.text == "Фурри😽")
async def furry(message: Message, state: FSMContext):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

    if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
        results = results3
        i = random.randint(0,len(results))
        zxc = results[i]
        asd = zxc["imageUrl"]
        await message.answer_photo(photo=asd)
    else:
        await message.answer("Подпишись на @HentaiTonBot чтобы бот мог работать!")
##########################################################




@router.message(F.text == "Готовые фото💾")
async def primeri(message: Message, state: FSMContext):
    photo = FSInputFile(os.path.join(media, "gotovo.jpg"))
    await message.answer_photo(photo=photo, caption="Тут ты можешь посмотреть уже готовые результаты генерации, разделенные по категориям", reply_markup=keyboard2())



@router.message(F.text == "Главное меню🏡")
async def glavnoe_menu(message: Message, state: FSMContext):
    await message.answer("Переход в главное меню", reply_markup=keyboard1())






########################################################################
@router.message(F.text == "Генерация🤖")
async def generate(message: Message, state: FSMContext):
    photo = FSInputFile(os.path.join(media, "gen.jpg"))
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

    if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
        
        await message.answer_photo(photo=photo,caption="Введите запрос для генерации\nнапример:\nФиолетовые волосы, косичка, раздвинутые ноги, и тд.")
        await state.set_state(Order.gen)
    else:
        await message.answer("Подпишись на @HentaiTonBot чтобы бот мог работать!")

@router.message(Order.gen)
async def generate2(message: Message, state: FSMContext):
    zapros = message.text
    if zapros not in ["Генерация🤖","Готовые фото💾","Профиль👤","Аниме🖊","Порно👩‍🦰","Фурри😽","Главное меню🏡"]:
        tokens = [
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2OTZiNzVhNDg5ZTMxZmRlMzQ2NDIwZCIsImRvbWFpbiI6Imh0dHBzOi8vd3d3LmNyZWF0ZWhlbnRhaS5jb20iLCJqdGkiOiI2Njk2Yjc1YTcwMzNlM2Y3YzgwY2IwMmMiLCJpYXQiOjE3MjExNTMzNzAsImV4cCI6MTcyMzc0NTM3MH0.C9cB8sFCkIejovyJjjCr2A67C0iUb9MK4P-aRPMQIuk",
                ""
                ]


        params = {"generator":"anime","tagGroups":[],"customPrompt":zapros,"queueType":0,"resolution":1}
        headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Content-Type': 'application/json',
                'Authorization':f'Bearer {tokens[0]}',
                'x-origin': 'https://www.createhentai.com',
                'Origin': 'https://www.createhentai.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.createhentai.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'Priority': 'u=1',
                'TE': 'trailers'
                }




        response = requests.post("https://api.createporn.com/generate/start", headers=headers, json=params)
        json = response.json()
        print(json)
    

        if response.status_code == 429:
            await message.answer("Кто-то уже генерирует🙁\nПодождите 3-5 минут⏰, и попробуйте еще раз🔄")
            await state.clear()

        if response.status_code == 200:
            await message.answer("Запрос успешно отправлен✅\nОжидайте 3-5 минут⏰")
            jobId= json['jobId']
            print(jobId)
            text123 = "Генерация"
            msg = await message.answer(text123)
            while True:
                text123 = text123 + "."
                async with ChatActionSender(bot = bot, chat_id = message.chat.id, action="upload_photo"):
                    await asyncio.sleep(50)
                params2 = {"jobId":jobId,"queueType":0}
                response2 = requests.post("https://api.createporn.com/generate/poll/", headers=headers, json=params2)
                json2 = response2.json()
                print(json2)

                if json2["status"] == "pending" or json2["status"] == "active" or json2["status"] == "delayed":
                    await bot.edit_message_text(text = text123, chat_id = message.chat.id, message_id = msg.message_id)
    
                if json2["status"] == "completed":
                    await bot.edit_message_text(text = "Готово✅", chat_id = message.chat.id, message_id = msg.message_id)
                    result = json2["result"]
                    await message.answer_photo(photo=result["image"])
                    break
#############################################################################












########################################################################

@router.message(F.text == "Профиль👤")
async def profile(message:Message, state:FSMContext):
    photo = FSInputFile(os.path.join(media, "profile.jpg"))
    await message.answer_photo(photo=photo,caption=f"""Твой профиль👤:\n
<b>Имя </b>🗣: {message.from_user.full_name}
<b>Запросов</b>💰: {check_balance(message.chat.id)[0]}
<b>Рефералов</b>👪:{check_referals(message.chat.id)[0]}

<b>Ваша реферальная ссылка:</b> \n<code>https://t.me/HentaiTon_bot?start={message.chat.id}</code>\n\n""",parse_mode=ParseMode.HTML)
    await state.clear()

