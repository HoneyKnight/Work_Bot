from config import update

url_global = (
    'https://russia.superjob.ru/vacancy/search/?'
    'keywords=python%2C%20django&remote_work_binary='
    '2&remote_work_no_geo=1&order_by%5Bupdated_at%5D=desc'
)


def check_update_superjob():
    return update(
        url_global=url_global,
        tag='span',
        tag_class='_26gg2 _3oXMw _2LaRg hbKbL rIDaO oDIMq _33qju _1ZV-S',
        site='superjob'
    )
