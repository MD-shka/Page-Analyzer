import requests
from .db_requests import get_url


def get_status_code(id):
    url_name = get_url(id).name
    status_code = requests.get(url_name).status_code
    return status_code
