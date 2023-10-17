import os
import logging

import src.helpers as h
import src.dataBase as db

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

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
        "📊 Показать статистику: /statistics \n\n"
        "🧩 Категории трат: /category\n\n"
        "📁 Выгрузить Excel файл: /excel")


@dp.message_handler(commands=["statistics"])
@secure_auth
async def show_statistics(message: types.Message):
    await message.answer(db.expense_data)


@dp.message_handler()
@secure_auth
async def add_expense(message: types.Message):
    try:
        expense = message.text.split()
        h.db_add_expense(expense[0],expense[1])
        await bot.send_message(message.chat.id, expense)
    except IndexError:
        await bot.send_message(message.chat.id, "Не понял тебя")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)