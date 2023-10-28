# Makefile

# Define common variables
DJANGO_MANAGE = python manage.py
CELERY_COMMAND = celery -A src
DOCKER_COMPOSE = docker-compose
DOCKER = docker
PYTHON := python
PIP := pip
BROWSER := firefox

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

rel_current_path = sys.argv[1]
abs_current_path = os.path.abspath(rel_current_path)
uri = "file://" + pathname2url(abs_current_path)

webbrowser.open(uri)
endef

export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

regex_pattern = r'^([a-zA-Z_-]+):.*?## (.*)$$'

for line in sys.stdin:
	match = re.match(regex_pattern, line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

# Additional rules can be added as needed.
.PHONY: prepare sudo migrate run up down ps purge whos which

help: ## Add a rule to list commands
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean-logs: # Add a rule to remove log info
	rm -fr build/ dist/ .eggs/
	find . -name '*.log' -o -name '*.log' -exec rm -fr {} +

clean-pyc: # Add a rule to remove pyc files
	find . -name '*.pyc' -o -name '*.pyo' -o -name '*~' -exec rm -rf {} +

clean-test: # remove test and coverage artifacts
	rm -fr .tox/ .testmondata* .coverage coverage.* htmlcov/ .pytest_cache

clean-cache: # remove test and coverage artifacts
	find . -name '*cache*' -exec rm -rf {} +

clean: clean-logs clean-pyc clean-test clean-cache ## Add a rule to remove unnecessary assets
	$(DOCKER) system prune --volumes -f

env: ## Add a rule to activate environment
	poetry shell

prepare: clean env ## Add a rule to activate environment and install dependencies

allow: ## Add a rule to allow scripts to execute
	chmod +x *

install: ## Add a rule to install project dependencies.
	poetry install

whos: ## Add a rule to list ports with certain port number
	@PORT_NUMBER=$(PORT_NUMBER) && \
    echo "$$(lsof -i ":$$PORT_NUMBER" | awk '{ print $$2 }' | awk 'NR>1')" | uniq -u

which: ## Add a rule to analyze ports with certain port number
	@PORT_NUMBER=$(PORT_NUMBER) && \
    lsof -i ":$$PORT_NUMBER" | \
	awk -F'\n' '{ print $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9 }' | \
	awk 'NR>1' | uniq -u

lint: ## Add a rule to clean up any temporary files
	black --skip-string-normalization .
	ruff --fix .
	pre-commit run --all-files
	find . -name "*.py" -exec autopep8 --in-place --aggressive --aggressive {} \;

test: ## Add a rule to test the application
	poetry run coverage run --rcfile=.coveragerc -m pytest --ignore=src/migrations

watch: env ## run tests on watchdog mode
	ptw . -- pytest --ignore=src/migrations

cov: clean test ## Add a rule to generate coverage report
	coverage report --omit="src/migrations/*" --show-missing

swagger: ## Add a rule to generate swagger in json format
	$(DJANGO_MANAGE) generate_swagger

schema: ## Add a rule to generate swagger in yaml format
	$(DJANGO_MANAGE) generateschema

report: coverage ## Add a rule to generate coverage report

html-report: clean test report ## Add a rule to generate coverage report
	coverage html --omit="src/migrations/*" --skip-covered
	$(BROWSER) htmlcov/index.html

migrate: # Add a rule to run initial migrations and create a superuser
	$(DJANGO_MANAGE) migrate

collect: # Add a rule to collect static files for production environment
	$(DJANGO_MANAGE) collectstatic

worker: # Add a rule to run celery worker
	$(CELERY_COMMAND) worker -l info 

flower: # Add a rule to run flower
	$(CELERY_COMMAND) flower

ps: ## Add a rule to list containers
	docker ps -a

build: ## Add a rule to build the docker containers
	$(DOCKER_COMPOSE) build

up: ## Add a rule to docker up containers
	$(DOCKER_COMPOSE) up

down: ## Add a rule to docker down containers
	$(DOCKER_COMPOSE) down

run: ## Add a rule to run the development server.
	$(DJANGO_MANAGE) runserver 0.0.0.0:8000

db-check: ## Add a rule to check database connection
	$(DJANGO_MANAGE) check

deploy: build up db-check ## Add a rule to deploy the server.

sudo: ## Add a rule to add Django super user
	$(DJANGO_MANAGE) createsuperuser

shell: ## Add a rule to collect static files for production environment
	$(DJANGO_MANAGE) shell
