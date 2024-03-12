import os
import psycopg2
from psycopg2.extras import NamedTupleCursor
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def connect():
    return psycopg2.connect(DATABASE_URL)


def make_request(*args, fetch=False, **kwargs):
    with connect() as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute(*args, **kwargs)
        if fetch:
            if fetch == "every":
                return curs.fetchall()
            elif fetch == "one":
                return curs.fetchone()
        return None


def is_unique_url(url):
    return make_request(
        'SELECT * FROM urls WHERE name=%s;',
        (url,),
        fetch="one"
    )


def get_url(id):
    return make_request(
        'SELECT * FROM urls WHERE id=%s;',
        (id,),
        fetch="one"
    )


def get_checks(id):
    return make_request(
        'SELECT * '
        'FROM url_checks '
        'WHERE url_id=%s '
        'ORDER BY url_checks.id DESC;',
        (id,),
        fetch="every"
    )


def get_urls():
    return make_request(
        "SELECT "
        "urls.id AS id, "
        "urls.name AS name, "
        "MAX(url_checks.created_at) AS last_check, "
        "url_checks.status_code AS status_code "
        "FROM urls "
        "JOIN url_checks ON urls.id = url_checks.url_id "
        "GROUP BY urls.id, urls.name, url_checks.status_code "
        "ORDER BY urls.id DESC;",
        fetch="every"
    )


def get_url_id(url):
    result = make_request(
        "SELECT * FROM urls WHERE name=%s;",
        (url,),
        fetch="one"
    )
    return result.id


def add_new_url(name_url):
    make_request(
        "INSERT INTO urls (name) VALUES (%s);",
        (name_url,)
    )


def add_check(url_id, status_code=None, h1=None, title=None, description=None):
    make_request(
        "INSERT INTO url_checks ("
        "url_id, "
        "status_code, "
        "h1, "
        "title, "
        "description) "
        "VALUES (%s, %s, %s, %s, %s);",
        (url_id, status_code, h1, title, description)
    )
