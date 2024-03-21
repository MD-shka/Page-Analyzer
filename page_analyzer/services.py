from .db_requests import (
    get_url,
    get_checks,
    get_urls,
    is_unique_url,
    add_new_url,
    add_check,
    get_url_id
)
from .url_validation import url_validation, url_normalization
from .parser import get_parse


def get_current_url_data(db_url, id):
    url = get_url(db_url, id)
    checks = get_checks(db_url, id)
    return url, checks


def get_list_urls_data(db_url):
    return get_urls(db_url)


def add_url_data(db_url, url):
    error_message = url_validation(url)
    if error_message:
        return None, error_message, 'danger'
    name_url = url_normalization(url)
    if not is_unique_url(db_url, name_url):
        add_new_url(db_url, name_url)
        return (
            get_url_id(db_url, name_url),
            'Страница успешно добавлена',
            'success'
        )
    return (
        get_url_id(db_url, name_url),
        'Страница уже существует',
        'info'
    )


def check_url_data(db_url, id):
    status_code, h1, title, description = get_parse(db_url, id)
    if status_code == 200:
        add_check(db_url, id, status_code, h1, title, description)
        return 'Страница успешно проверена', 'success'
    return 'Произошла ошибка при проверке', 'danger'
