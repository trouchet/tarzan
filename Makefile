# Makefile

# Define common variables
DJANGO_MANAGE = python manage.py
DOCKER_COMPOSE = docker-compose
DOCKER = docker
PYTHON := python
PIP := pip

# Additional rules can be added as needed.
.PHONY: prepare sudo migrate run up down ps purge 

env: ## Add a rule to activate environment
	poetry shell

install: ## Add a rule to install project dependencies.
	poetry install

prepare: clean env install # Add a rule to activate environment and install dependencies

clean: ## Add a rule to clean up any temporary files
	find . -name "*.pyc" -exec rm -f {} \;
	rm -rf venv

migrate: ## Add a rule to run initial migrations and create a superuser
	$(DJANGO_MANAGE) migrate

collect: ## Add a rule to collect static files for production environment
	$(DJANGO_MANAGE) collectstatic

shell: ## Add a rule to collect static files for production environment
	$(DJANGO_MANAGE) shell

ps: ## Add a rule to list containers
	docker ps -a

build: ## Add a rule to run initial migrations and create a superuser
	$(DOCKER_COMPOSE) build

up: ## Add a rule to docker up container
	$(DOCKER_COMPOSE) up -d

down: ## Add a rule to docker down container
	$(DOCKER_COMPOSE) down

run: ## Add a rule to run the development server.
	$(DJANGO_MANAGE) runserver 0.0.0.0:8000

deploy: build up migrate collect run ## Add a rule to deploy the server.

sudo: ## Add a rule to add Django super user
	$(DJANGO_MANAGE) createsuperuser
