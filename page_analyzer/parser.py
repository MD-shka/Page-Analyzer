import requests
from .db_requests import get_url
from bs4 import BeautifulSoup


def get_parse(db_url, id):
    response = requests.get(get_url(db_url, id).name)
    status_code = response.status_code
    html = BeautifulSoup(response.text, features="html.parser")
    h1 = html.find("h1").text
    title = html.title.string
    description = html.find('meta', {'name': 'description'})['content']
    return status_code, h1, title, description
