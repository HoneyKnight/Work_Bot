import asyncio
import os
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from dotenv import load_dotenv

from db import Vacancies, session
from habr import check_update_habr, check_update_habr_local
from hh import check_update_hh, check_update_hh_global, check_update_hh_local
from rabota_ru import check_update_rabota

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = [
        "Свежие вакансии",
        "Загрузить данные",
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента вакансий", reply_markup=keyboard)


@dp.message_handler(Text(equals="Загрузить данные"))
async def get_data(message: types.Message):
    while True:
        check_update_hh(),
        check_update_habr(),
        check_update_rabota(),
        check_update_hh_local(),
        check_update_habr_local(),
        check_update_hh_global()
        await message.answer("Загрузка вакансий прошла успешно")
        await asyncio.sleep(900)


@dp.message_handler(Text(equals="Свежие вакансии"))
async def send_message_with_vacancies(message: types.Message):
    while True:
        queryset = session.query(Vacancies).filter(
            Vacancies.created_at > datetime.now() - timedelta(seconds=600)
        )
        if queryset.count() >= 1:
            for vacancy in queryset:
                vacancies = (
                    f'{hlink(vacancy.vacancy_name, vacancy.vacancy_url)}'
                )

                await message.answer(vacancies, parse_mode='HTML')
                await asyncio.sleep(1)

        await message.answer("Пока нет свежих вакансий...")
        await asyncio.sleep(600)


if __name__ == '__main__':
    executor.start_polling(dp)
    loop = asyncio.get_event_loop()
    loop.create_task(
        get_data(),
        send_message_with_vacancies()
    )
