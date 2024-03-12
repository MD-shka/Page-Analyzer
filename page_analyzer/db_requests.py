import os
import psycopg2
from psycopg2.extras import NamedTupleCursor
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def connect():
    return psycopg2.connect(DATABASE_URL)


def make_request(request, params):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute(request, params)
        result = curs.fetchone()
    return result


def is_unique_url(url):
    result = make_request('SELECT * FROM urls WHERE name=%s;', (url,))
    if result:
        return False
    return True


def get_url(id):
    result = make_request('SELECT * FROM urls WHERE id=%s;', (id,))
    return result


def get_checks(id):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM url_checks WHERE url_id=%s ORDER BY url_checks.id DESC;', (id,))
        checks = curs.fetchall()
    return checks


def get_urls():
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute(f"SELECT "
                     f"urls.id AS id, "
                     f"urls.name AS name, "
                     f"MAX(url_checks.created_at) AS last_check, "
                     f"url_checks.status_code AS status_code "
                     f"FROM urls "
                     f"JOIN url_checks ON urls.id = url_checks.url_id "
                     f"GROUP BY urls.id, urls.name, url_checks.status_code "
                     f"ORDER BY urls.id DESC;")
        urls = curs.fetchall()
    return urls


def get_url_id(url):
    result = make_request('SELECT * FROM urls WHERE name=%s;', (url,))
    return result.id


def add_new_url(name_url):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('INSERT INTO urls (name) VALUES (%s);', (name_url,))
        conn.commit()


def add_check(url_id, status_code=None, h1=None, title=None, description=None):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('INSERT INTO url_checks (url_id, status_code, h1, title, description)'
                     'VALUES (%s, %s, %s, %s, %s);', (url_id, status_code, h1, title, description))
        conn.commit()
