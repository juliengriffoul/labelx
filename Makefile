PROJECT=labelx
TESTS=tests

USER_OR_VENV := --user
ifdef VIRTUAL_ENV
USER_OR_VENV :=
endif

.DEFAULT_GOAL := all

all: install test-cov

install: clean
	python setup.py install $(USER_OR_VENV)

lint:
	pylint $(PROJECT) $(TESTS)

test: clean-pyc
	pytest --verbose --color=yes $(TESTS)

reports-init:
	mkdir -p reports

test-cov: reports-init
	pytest --cov-report term --cov-report xml:reports/coverage-report.xml --cov=$(PROJECT) $(TESTS) && coverage xml -o reports/coverage-report.xml

clean-pyc:
	find . \( -name __pycache__ -o -name *.pyc -o -name *.pyo -o -name *~ \) -exec rm -rf {} +

clean: clean-pyc
	rm -rf .coverage build dist *.spec *.egg-info .pytest_cache *.egg-info dist-binary

run:
	FLASK_APP=$(PROJECT)/main.py FLASK_ENV=development flask run
