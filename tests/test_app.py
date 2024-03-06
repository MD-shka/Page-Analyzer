import pytest
from page_analyzer.app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_get_index(client):
    response = client.get('/')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Анализатор страниц' in text_page
    assert 'Бесплатно проверяйте сайты на SEO-пригодность' in text_page
