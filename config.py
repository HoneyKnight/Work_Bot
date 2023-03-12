import json
import os

import requests
from aiogram import Bot, Dispatcher
from aiogram.utils.markdown import hlink
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fake_useragent import UserAgent

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', default='your bot token')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

path_file = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'vacancies_dict.json'
)

useragent = UserAgent()

headers = {
    'user-agent': f'{useragent.random}'
}


def get_vacansies_dict():
    vacancies_dict = {}

    with open('vacancies_dict.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)


def update(url_global, tag, tag_class, site):
    with open("vacancies_dict.json", encoding='utf-8') as file:
        vacancies_dict = json.load(file)

    fresh_vacancies = {}

    request = requests.get(url=url_global, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    all_vacancies = soup.find_all(tag, class_=tag_class)

    for vacancy in all_vacancies:
        vacancy_url = f'{vacancy.get("href")}'
        if site == 'hh':
            vacancy_id = vacancy_url.replace('?', '/').split('/')[-2] + 'hh'
        if site == 'habr':
            vacancy_url = f'https://career.habr.com{vacancy.get("href")}'
            vacancy_id = vacancy_url.split('/')[-1] + 'habr'
        if site == 'superjob':
            vacancy_next = vacancy.find_next('a')
            vacancy_url = f'https://russia.superjob.ru{vacancy_next.get("href")}'
            vacancy_id = vacancy_url.replace('.', '-').split('-')[-2] + 'superjob'
            vacancy_name = vacancy_next.text
        if site == 'rabota_ru':
            vacancy_url = f'https://nn.rabota.ru{vacancy.get("href")}'
            vacancy_id = vacancy_url.split('/')[-2] + 'rabota_ru'

        if vacancy_id in vacancies_dict:
            continue
        elif site == 'superjob':
            vacancy_name = vacancy_next.text
        vacancy_name = vacancy.text.strip()

        vacancies_dict[vacancy_id] = {
            'vacancy_name': vacancy_name,
            'vacancy_url': vacancy_url
        }

        fresh_vacancies[vacancy_id] = {
            'vacancy_name': vacancy_name,
            'vacancy_url': vacancy_url
        }

    with open('vacancies_dict.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)

    if len(vacancies_dict) > 1000:
        os.remove(path_file)
        get_vacansies_dict()

    return fresh_vacancies


async def get_vacancies(message, frash_vacancies):
    frash_vacancies = frash_vacancies
    if len(frash_vacancies) >= 1:
        for key, value in sorted(frash_vacancies.items()):
            vacancies = f"{hlink(value['vacancy_name'], value['vacancy_url'])}"

            await message.answer(vacancies, parse_mode='HTML')

    await message.answer("Пока нет свежих вакансий...")
