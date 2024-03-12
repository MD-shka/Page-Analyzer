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


def get_urls():
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM urls ORDER BY  id DESC;')
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
