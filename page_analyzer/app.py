import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    flash,
    get_flashed_messages,
    redirect,
    url_for,
    abort
)
from .url_validation import url_validation, url_normalization
from .db_requests import (
    is_unique_url,
    get_url_id,
    add_new_url,
    get_urls,
    get_url,
    add_check,
    get_checks
)
from .parser import get_parse


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/")
def index():
    return render_template('index.html')


@app.get("/urls/<int:id>")
def get_current_url(id):
    url = get_url(id)
    checks = get_checks(id)
    if url is None:
        page_not_found(404)
    return render_template(
        'url.html',
        url=url,
        checks=checks,
        message=get_flashed_messages(with_categories=True)
    )


@app.get("/urls")
def get_list_urls():
    urls = get_urls()
    return render_template(
        'urls.html',
        urls=urls,
        message=get_flashed_messages(with_categories=True)
    )


@app.post("/urls")
def add_url():
    url = request.form['url']
    error_message = url_validation(url)
    if error_message:
        flash(error_message, 'danger')
        return render_template(
            'index.html',
            url=url,
            message=get_flashed_messages(with_categories=True)
        ), 422
    name_url = url_normalization(url)
    if not is_unique_url(name_url):
        flash('Страница успешно добавлена', 'success')
        add_new_url(name_url)
    else:
        flash('Страница уже существует', 'info')
    return redirect(url_for('get_current_url', id=get_url_id(name_url)))


@app.post("/urls/<int:id>/checks")
def check_url(id):
    status_code, h1, title, description = get_parse(id)
    if status_code == 200:
        flash('Страница успешно проверена', 'success')
        add_check(id, status_code, h1, title, description)
    else:
        flash('Произошла ошибка при проверке', 'danger')
    return redirect(url_for('get_current_url', id=id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404
