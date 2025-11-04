import asyncio
import logging
import os
import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from getdata import getDay,getMessage, calculateDate

load_dotenv()

logging.basicConfig(level=logging.INFO)

router = Router()

bot = Bot(token=os.getenv("BOT_TOKEN"))

userDict={}

    

kb_list = [
    [KeyboardButton(text="Сменить неделю")],
    [KeyboardButton(text="Сегодня",), KeyboardButton(text="Завтра")],
    [KeyboardButton(text="ПН"), KeyboardButton(text="ВТ"), KeyboardButton(text="СР")],
    [KeyboardButton(text="ЧТ"), KeyboardButton(text="ПТ"), KeyboardButton(text="СБ")],
]

main_kb = ReplyKeyboardMarkup(keyboard=kb_list,resize_keyboard=True)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    userDict[message.from_user.id] = 1
    await message.answer("""
Привет! Я бот с расписанием.
Сейчас доступно только распиание группы 1-45м.
Для навигации использу клавиатуру снизу.
По умолччанию выбрана первая неделя""",reply_markup=main_kb)

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = """
Доступные команды:
/start - Начать работу
/help - Сообщения с командами
"""
    await message.answer(help_text)

@router.message(lambda message: message.text == "Сменить неделю")
async def change_week(message: types.Message):
    value = userDict[message.from_user.id]
    match value:
        case 0:
            userDict[message.from_user.id] = 1
            await message.answer("Выбрана вторая неделя")
        case 1:
            userDict[message.from_user.id] = 0
            await message.answer("Выбрана первая неделя")


@router.message(lambda message: message.text == "Сегодня")
async def get_today(message: types.Message):
    week, day = calculateDate(0)
    text = getMessage(week,day)
    await message.answer(f"{text}")
    

@router.message(lambda message: message.text == "Завтра")
async def get_tomorrow(message: types.Message):
    week,day = calculateDate(1)
    text = getMessage(week,day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "ПН")
async def get_monday(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "ВТ")
async def get_thuesday(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "СР")
async def get_wednesday(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "ЧТ")
async def get_thuersay(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "ПТ")
async def get_friday(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")

@router.message(lambda message: message.text == "СБ")
async def get_saturday(message: types.Message):
    day = getDay(message.text)
    week = userDict.get(message.from_user.id, 1)
    text = getMessage(week, day)
    await message.answer(f"{text}")




async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
