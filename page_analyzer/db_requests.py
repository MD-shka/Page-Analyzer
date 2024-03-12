import os
import psycopg2
from psycopg2.extras import NamedTupleCursor
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def connect():
    return psycopg2.connect(DATABASE_URL)


def is_unique_url(url):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM urls WHERE name=%s;', (url,))
        result = curs.fetchone()
    if result:
        return False
    return True


def get_url(id):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM urls WHERE id=%s;', (id,))
        result = curs.fetchone()
    return result


def get_urls():
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM urls ORDER BY  id DESC;')
        urls = curs.fetchall()
    return urls


def get_url_id(url):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('SELECT * FROM urls WHERE name=%s;', (url,))
        result = curs.fetchone()
    return result.id


def add_new_url(name_url):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute('INSERT INTO urls (name) VALUES (%s);', (name_url,))
        conn.commit()
