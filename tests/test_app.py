import pytest
from page_analyzer.app import app as flask_app


@pytest.fixture
def app():
    app = flask_app
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_index(client):
    response = client.get('/')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Анализатор страниц' in text_page
    assert 'Бесплатно проверяйте сайты на SEO-пригодность' in text_page


def test_add_url(client):
    response = client.post('/urls', data={'url': 'https://ru.hexlet.io'})
    assert response.status_code == 302


def test_get_current_url(client):
    response = client.get('/urls/1')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Сайт' in text_page
    assert 'Проверки' in text_page


def test_get_list_urls(client):
    response = client.get('/urls')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Сайты' in text_page
    assert 'Последняя проверка' in text_page


def test_check_url(client):
    response = client.post('/urls/1/checks')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 302
    assert 'title'in text_page


def test_page_not_found(client):
    response = client.get('/not_found')
    text_page = response.data.decode('utf-8')
    assert response.status_code == 404
    assert 'Здесь нет того, что вы ищете' in text_page
