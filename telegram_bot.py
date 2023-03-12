from aiogram import executor, types
from aiogram.dispatcher.filters import Text

from config import dp, get_vacancies
from habr import check_update_habr, check_update_habr_local
from hh import check_update_hh, check_update_hh_local
from rabota_ru import check_update_rabota
from superjob import check_update_superjob


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = [
        "Свежие вакансии России",
        "Свежие вакансии Нижнего Новгорода"
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента вакансий", reply_markup=keyboard)


@dp.message_handler(Text(equals="Свежие вакансии России"))
def get_global_vacancies(message: types.Message):
    return get_vacancies(
        message=message,
        frash_vacancies={
            **check_update_hh(),
            **check_update_habr(),
            **check_update_superjob(),
            **check_update_rabota(),
        }
    )


@dp.message_handler(Text(equals="Свежие вакансии Нижнего Новгорода"))
def get_local_vacancies(message: types.Message):
    return get_vacancies(
        message=message,
        frash_vacancies={
            **check_update_hh_local(),
            **check_update_habr_local()
        }
    )


if __name__ == '__main__':
    executor.start_polling(dp)
