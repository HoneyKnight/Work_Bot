import asyncio
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from dotenv import load_dotenv

from habr import check_update_habr, check_update_habr_local
from hh import check_update_hh, check_update_hh_local
from rabota_ru import check_update_rabota
from superjob import check_update_superjob

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = [
        "Свежие вакансии",
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента вакансий", reply_markup=keyboard)


@dp.message_handler(Text(equals="Свежие вакансии"))
async def get_fresh_vacancies(message: types.Message):
    while True:
        frash_vacancies = {
            **check_update_hh(),
            **check_update_habr(),
            **check_update_superjob(),
            **check_update_rabota(),
            **check_update_hh_local(),
            **check_update_habr_local()
        }

        if len(frash_vacancies) >= 1:
            for k, v in sorted(frash_vacancies.items()):
                vacancies = f"{hlink(v['vacancy_name'], v['vacancy_url'])}"

                await message.answer(vacancies, parse_mode='HTML')

        else:
            await message.answer("Пока нет свежих вакансий...")

        await asyncio.sleep(15)


if __name__ == '__main__':
    executor.start_polling(dp)
    loop = asyncio.get_event_loop()
    loop.create_task(get_fresh_vacancies())
