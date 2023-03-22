from general_function import update

url_global = (
    'https://nn.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=%28Back'
    '-end+OR+Backend+OR+%D0%B1%D1%8D%D0%BA%D1%8D%D0%BD%D0%B4+OR+%D0%B1%D0%B5%D0%'
    'BA%D0%B5%D0%BD%D0%B4+OR+%D0%B1%D1%8D%D0%BA%D0%B5%D0%BD%D0%B4+OR+Python+OR+%'
    'D0%BF%D0%B8%D1%82%D0%BE%D0%BD+OR+%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD+OR+%D'
    '0%94%D0%B6%D0%B0%D0%BD%D0%B3%D0%BE+OR+DRF+OR+Django%29+AND+%28Developer+OR+'
    '%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA+OR+'
    'Engineer+OR+Programmer+OR+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%'
    'D0%B8%D1%81%D1%82+OR+%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%'
    'D1%82%29+AND+NOT+%28Java+OR+C%2B%2B+OR+C%23+OR+PHP+OR+Frontend+OR+GO+OR+Node'
    '.js+OR+Golang+OR+.Net+OR+IOS+OR+Laravel%29&excluded_text=&salary=&'
    'currency_code=RUR&experience=doesNotMatter&schedule=remote&order_by='
    'publication_time&search_period=0&items_on_page=20'
)

url_local = (
    'https://nn.hh.ru/search/vacancy?text=%28Back-end+OR+Backend+OR+%D0%B1%D1%8D%D'
    '0%BA%D1%8D%D0%BD%D0%B4+OR+%D0%B1%D0%B5%D0%BA%D0%B5%D0%BD%D0%B4+OR+%D0%B1%D1%8'
    'D%D0%BA%D0%B5%D0%BD%D0%B4+OR+Python+OR+%D0%BF%D0%B8%D1%82%D0%BE%D0%BD+OR+%D0%'
    'BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD+OR+%D0%94%D0%B6%D0%B0%D0%BD%D0%B3%D0%BE+OR+D'
    'RF+OR+Django%29+AND+%28Developer+OR+%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%B'
    'E%D1%82%D1%87%D0%B8%D0%BA+OR+Engineer+OR+Programmer+OR+%D0%BF%D1%80%D0%BE%D0%'
    'B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+OR+%D1%81%D0%BF%D0%B5%D1%86%D0%B'
    '8%D0%B0%D0%BB%D0%B8%D1%81%D1%82%29+AND+NOT+%28PHP+OR+JAVA+OR+Android+OR+C%2B%'
    '2B%29&salary=&area=66&no_magic=true&ored_clusters=true&order_by=publication_time'
    '&excluded_text='
)

url_global_2 = (
    'https://nn.hh.ru/search/vacancy?text=%28Back-end+OR+Backend+OR+%D0%B1%D1%8D%D0%'
    'BA%D1%8D%D0%BD%D0%B4+OR+%D0%B1%D0%B5%D0%BA%D0%B5%D0%BD%D0%B4+OR+%D0%B1%D1%8D%D0'
    '%BA%D0%B5%D0%BD%D0%B4+OR+Python+OR+%D0%BF%D0%B8%D1%82%D0%BE%D0%BD+OR+%D0%BF%D0%'
    'B0%D0%B9%D1%82%D0%BE%D0%BD+OR+%D0%94%D0%B6%D0%B0%D0%BD%D0%B3%D0%BE+OR+DRF+OR+'
    'Django%29+AND+%28Developer+OR+%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%'
    'D1%87%D0%B8%D0%BA+OR+Engineer+OR+Programmer+OR+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D'
    '0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+OR+%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%B'
    'B%D0%B8%D1%81%D1%82%29+AND+NOT+%28Flask+OR+fastAPI+OR+fast-api+OR+C%2B%2B+OR+PHP'
    '+OR+JAVA+OR+IOS+OR+Node.js+OR+C%23+OR+Go+OR+Golang+OR+Kotlin+OR+Ruby+OR+%D0%A4%D'
    '1%80%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D0%B4+OR+Scala+OR+DevOps%29&salary=&area=113&'
    'saved_search_id=64266023&no_magic=true&ored_clusters=true&date_from=13.03.2023+16'
    '%3A26%3A30&experience=between1And3'
)


def check_update_hh():
    return update(
        url_global=url_global,
        tag='a',
        tag_class='serp-item__title',
        site='hh'
    )


def check_update_hh_local():
    return update(
        url_global=url_local,
        tag='a',
        tag_class='serp-item__title',
        site='hh'
    )


def check_update_hh_global():
    return update(
        url_global=url_global_2,
        tag='a',
        tag_class='serp-item__title',
        site='hh'
    )
