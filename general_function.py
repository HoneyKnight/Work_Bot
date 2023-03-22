from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from db import Vacancies, session

useragent = UserAgent()

headers = {
    'user-agent': f'{useragent.random}'
}


def update(url_global, tag, tag_class, site):

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
        if site == 'rabota_ru':
            vacancy_url = f'https://nn.rabota.ru{vacancy.get("href")}'
            vacancy_id = vacancy_url.split('/')[-2] + 'rabota_ru'
        vacancy_name = vacancy.text.strip()

        if session.query(Vacancies).filter(
            Vacancies.vacancy_id == vacancy_id
        ).all():
            continue

        vacancies = Vacancies(
            vacancy_id=vacancy_id,
            vacancy_name=vacancy_name,
            vacancy_url=vacancy_url,
            created_at=datetime.now(),
        )
        session.add(vacancies)

    session.query(Vacancies).filter(
        Vacancies.created_at < datetime.now() - timedelta(hours=10)
    ).delete(synchronize_session='fetch')
    session.commit()

    session.close()
