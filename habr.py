from general_function import update

url_global = (
    'https://career.habr.com/vacancies?q=python&remote=true&sort=date&type=all'
)

url_local = (
    'https://career.habr.com/vacancies?sort=date&type=suitable'
)


def check_update_habr():
    return update(
        url_global=url_global,
        tag='a',
        tag_class='vacancy-card__title-link',
        site='habr'
    )


def check_update_habr_local():
    return update(
        url_global=url_local,
        tag='a',
        tag_class='vacancy-card__title-link',
        site='habr'
    )
