from abc import ABC, abstractmethod
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from db import Vacancies, session

useragent = UserAgent()

headers = {
    'user-agent': f'{useragent.random}'
}


class WorkingSite(ABC):
    @abstractmethod
    def get_vacancy_url(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_id(self, vacancy_url):
        pass

    def get_vacancy_name(self, vacancy):
        return vacancy.text.strip()


class HeadHunter(WorkingSite):
    def get_vacancy_url(self, vacancy):
        return f'{vacancy.get("href")}'

    def get_vacancy_id(self, vacancy_url):
        return vacancy_url.replace('?', '/').split('/')[-2] + 'hh'


class HabrCareer(WorkingSite):
    def get_vacancy_url(self, vacancy):
        return f'https://career.habr.com{vacancy.get("href")}'

    def get_vacancy_id(self, vacancy_url):
        return vacancy_url.split('/')[-1] + 'habr'


class RabotaRu(WorkingSite):
    def get_vacancy_url(self, vacancy):
        return f'https://nn.rabota.ru{vacancy.get("href")}'

    def get_vacancy_id(self, vacancy_url):
        return vacancy_url.split('/')[-2] + 'rabota_ru'


class Vacancy:
    def __init__(self, working_site: WorkingSite):
        self.site_state = working_site

    def create(self, vacancy):
        vacancy_url = self.site_state.get_vacancy_url(vacancy)
        vacancy_id = self.site_state.get_vacancy_id(vacancy_url)
        vacancy_name = self.site_state.get_vacancy_name(vacancy)

        if session.query(Vacancies).filter(
            Vacancies.vacancy_id == vacancy_id
        ).all():
            return None

        vacancies = Vacancies(
            vacancy_id=vacancy_id,
            vacancy_name=vacancy_name,
            vacancy_url=vacancy_url,
            created_at=datetime.now(),
        )
        session.add(vacancies)
        return vacancies


def update(working_site: WorkingSite, url_global, tag, tag_class):
    request = requests.get(url=url_global, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    all_vacancies = soup.find_all(tag, class_=tag_class)
    vacancy = Vacancy(working_site)

    for vacancy_data in all_vacancies:
        vacancies = vacancy.create(vacancy_data)
        if vacancies is not None:
            session.add(vacancies)

    session.query(Vacancies).filter(
        Vacancies.created_at < datetime.now() - timedelta(hours=10)
    ).delete(synchronize_session='fetch')
    session.commit()
