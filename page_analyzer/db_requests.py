import psycopg2
from psycopg2.extras import NamedTupleCursor


def connect(db_url):
    return psycopg2.connect(db_url)


def make_request(db_url, *args, fetch=None, **kwargs):
    with connect(db_url) as conn:
        curs = conn.cursor(cursor_factory=NamedTupleCursor)
        curs.execute(*args, **kwargs)
        if fetch:
            if fetch == "every":
                return curs.fetchall()
            elif fetch == "one":
                return curs.fetchone()
        return None


def is_unique_url(db_url, url):
    return make_request(
        db_url,
        'SELECT * FROM urls WHERE name=%s;',
        (url,),
        fetch="one"
    )


def get_url(db_url, id):
    return make_request(
        db_url,
        'SELECT * FROM urls WHERE id=%s;',
        (id,),
        fetch="one"
    )


def get_checks(db_url, id):
    return make_request(
        db_url,
        'SELECT * '
        'FROM url_checks '
        'WHERE url_id=%s '
        'ORDER BY url_checks.id DESC;',
        (id,),
        fetch="every"
    )


def get_urls(db_url):
    return make_request(
        db_url,
        "SELECT urls.id AS id, "
        "urls.name AS name, "
        "MAX(url_checks.created_at) AS last_check, "
        "url_checks.status_code AS status_code "
        "FROM urls LEFT JOIN url_checks ON urls.id = url_checks.url_id "
        "GROUP BY urls.id, urls.name, url_checks.status_code "
        "ORDER BY urls.id DESC;",
        fetch="every"
    )


def get_url_id(db_url, url):
    result = make_request(
        db_url,
        "SELECT * FROM urls WHERE name=%s;",
        (url,),
        fetch="one"
    )
    return result.id


def add_new_url(db_url, name_url):
    make_request(db_url, "INSERT INTO urls (name) VALUES (%s);", (name_url,))


def add_check(db_url, url_id, status_code, h1, title, description):
    make_request(
        db_url,
        "INSERT INTO url_checks ("
        "url_id, "
        "status_code, "
        "h1, "
        "title, "
        "description) "
        "VALUES (%s, %s, %s, %s, %s);",
        (url_id, status_code, h1, title, description)
    )
