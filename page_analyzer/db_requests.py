import os
import psycopg2
from psycopg2.extras import NamedTupleCursor
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def is_unique_url(url):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('SELECT * FROM urls WHERE name=%s;', (url,))
        result = curs.fetchone()
    conn.close()
    if result:
        return False
    return True


def get_url(id):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('SELECT * FROM urls WHERE id=%s;', (id,))
        result = curs.fetchone()
    conn.close()
    return result


def get_urls():
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('SELECT * FROM urls ORDER BY  id DESC;')
        urls = curs.fetchall()
    conn.close()
    return urls


def get_url_id(url):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('SELECT * FROM urls WHERE name=%s;', (url,))
        result = curs.fetchone()
    conn.close()
    return result.id


def add_new_url(name_url):
    conn = psycopg2.connect(DATABASE_URL)
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute('INSERT INTO urls (name) VALUES (%s);', (name_url,))
    conn.commit()
    conn.close()
