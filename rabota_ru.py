from main import RabotaRu, update

url_global = (
    'https://nn.rabota.ru/vacancy/?query=python&sort=relevance&specia'
    'lization_ids=2644&period=month&all_regions=1'
)


def check_update_rabota():
    return update(
        working_site=RabotaRu(),
        url_global=url_global,
        tag='a',
        tag_class='vacancy-preview-card__title_border',
    )
