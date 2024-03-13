import requests
from .db_requests import get_url
from bs4 import BeautifulSoup


def get_parse(id):
    response = requests.get(get_url(id).name)
    status_code = response.status_code
    html = BeautifulSoup(response.text, features="html.parser")
    title = html.title.string
    h1 = html.find("h1").text
    description = html.find('meta', {'name': 'description'})['content']
    return status_code, title, h1, description
