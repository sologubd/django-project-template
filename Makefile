compile-deps:
	pip-compile requirements.in

compile-deps-dev:
	pip-compile requirements-dev.in

sync-deps:
	pip-sync requirements.txt requirements-dev.txt

start:
	cd ./src && python manage.py runserver

lint:
	cd ./src && isort . && black .

generate-cov:
	coverage run -m pytest ./src && coverage html && open htmlcov/index.html

cov-report:
	pytest --cov-report term --cov=${app} ./src
