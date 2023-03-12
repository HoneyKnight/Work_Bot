from config import update

url_global = 'https://nn.rabota.ru/vacancy/?query=python&sort=relevance&specialization_ids=2644&period=month&all_regions=1'


def check_update_rabota():
    return update(
        url_global=url_global,
        tag='a',
        tag_class='vacancy-preview-card__title_border',
        site='rabota_ru'
    )
