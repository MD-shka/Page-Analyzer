from validators import url as is_valid
from urllib.parse import urlparse, urlunparse


def url_normalization(url):
    url_parse = urlparse(url)
    url_name = urlunparse((url_parse.scheme, url_parse.netloc, '', '', '', ''))
    return url_name


def url_validation(url):
    error = None
    if len(url) > 255:
        error = 'URL превышает 255 символов'
    elif not is_valid(url):
        error = 'Некорректный URL'
    return error
