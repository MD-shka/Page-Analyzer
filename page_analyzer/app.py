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
from .services import (
    get_current_url_data,
    get_list_urls_data,
    add_url_data,
    check_url_data
)


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/")
def index():
    return render_template('index.html')


@app.get("/urls/<int:id>")
def get_current_url(id):
    url, checks = get_current_url_data(DATABASE_URL, id)
    if url is None:
        abort(404)
    return render_template(
        'url.html',
        url=url,
        checks=checks,
        message=get_flashed_messages(with_categories=True)
    )


@app.get("/urls")
def get_list_urls():
    urls = get_list_urls_data(DATABASE_URL)
    return render_template(
        'urls.html',
        urls=urls,
        message=get_flashed_messages(with_categories=True)
    )


@app.post("/urls")
def add_url():
    url = request.form['url']
    url_id, message, category = add_url_data(DATABASE_URL, url)
    flash(message, category)
    if url_id:
        return redirect(url_for('get_current_url', id=url_id))
    return render_template(
        'index.html',
        url=url,
        message=get_flashed_messages(with_categories=True)
    ), 422


@app.post("/urls/<int:id>/checks")
def check_url(id):
    message, category = check_url_data(DATABASE_URL, id)
    flash(message, category)
    return redirect(url_for('get_current_url', id=id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404
