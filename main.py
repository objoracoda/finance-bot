import os
import logging

import src.helpers as helpers

import db as DB

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InputFile

TELEGRAM_API_TOKEN = os.getenv('MY_TELEGRAM_TOKEN', 'Token Not found')


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)


def secure_auth(func):
    async def wrapper(message):
        if message['from']['id'] != 673084689:
            return await message.reply("Access Denied",reply=False)
        return await func(message)
    return wrapper


@dp.message_handler(commands=["start","help"])
@secure_auth
async def welcome_msg(message: types.Message):
    await message.answer(
        "💸 Привет! Я Бот для учета твоих финансов!\n\n"
        "💵 Добавить расход: 100р Саня\n\n"
        "📊 Начать новый месяц: /null \n\n"
        "🧩 Категории трат: /category\n\n"
        "📁 Выгрузить Excel файл: /excel")



@dp.message_handler(commands=["null"])
@secure_auth
async def set_new_mounth(message: types.Message):
    helpers.add_excel(DB.sql_show_table(con))
    DB.sql_new_mounth(con)
    await message.answer_document(InputFile("fin.xlsx"))


@dp.message_handler(commands=["category"])
@secure_auth
async def show_category(message: types.Message):
    categorys = helpers.show_category(DB.sql_show_table(con))
    await message.answer(categorys)


@dp.message_handler(commands=["excel"])
@secure_auth
async def send_excel_table(message: types.Message):
    helpers.add_excel(DB.sql_show_table(con))
    await message.answer_document(InputFile("fin.xlsx"))


@dp.message_handler()
@secure_auth
async def add_expense(message: types.Message):
    try:
        expense = helpers.parse_expense(message.text)
        DB.sql_update(con,expense)
        await bot.send_message(message.chat.id, f"Записал {expense[0]}р в категорию {expense[1]} 👀")
    except IndexError:
        await bot.send_message(message.chat.id, "Не понял тебя")



if __name__ == '__main__':
    con = DB.connect()
    executor.start_polling(dp, skip_updates=True)