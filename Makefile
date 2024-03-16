#PORT ?= 8000


build:
	./build.sh

install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app run

start:
	poetry run python -c "from dotenv import load_dotenv; load_dotenv('.env'); import os; os.system('gunicorn -w 5 -b 127.0.0.1:' + os.getenv('PORT') + ' page_analyzer:app')"

lint:
	poetry run flake8 page_analyzer

test:
	poetry run pytest -vv

 test-coverage:
	poetry run pytest --cov=page_analyzer --cov-report xml

test-coverage-percent:
	pytest -vv --cov=/home/project_page_analyzer/python-project-83 --cov-report term-missing

rec:
	asciinema rec

selfcheck:
	poetry check

 check: selfcheck test lint

.PHONY: install test lint selfcheck check