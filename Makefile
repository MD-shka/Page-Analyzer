PORT ?= 8000


install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app run

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

lint:
	poetry run flake8 page_analyzer

# test:
# 	poetry run pytest

# test-coverage:
#	poetry run pytest --cov=gendiff --cov-report xml

# test-coverage-percent:
# 	pytest -vv --cov=/home/project_gendiff/python-project-50 --cov-report term-missing

rec:
	asciinema rec

# selfcheck:
# 	poetry check

# check: selfcheck test lint

.PHONY: install test lint selfcheck check build