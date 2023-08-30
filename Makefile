# Makefile

# Define common variables
DJANGO_MANAGE = python manage.py
DOCKER_COMPOSE = docker-compose
PYTHON := python
PIP := pip

# Additional rules can be added as needed.
.PHONY: venv install setup run clean test migrate migrate_periodic

# Add a rule to activate environment
shell:
	poetry shell

# Add a rule to install project dependencies.
install:
	poetry install

# Add a rule to activate environment and install dependencies
prepare: shell install

# Add a rule to clean up any temporary files.
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rmdir {} \;
	rm -rf venv

# Add a rule to run initial migrations and create a superuser.
migrate:
	$(DJANGO_MANAGE) migrate

# Add a rule to add Django super user
sudo:
	$(DJANGO_MANAGE) createsuperuser

# Add a rule to docker up container
up:
	$(DOCKER_COMPOSE) up -d

# Add a rule to docker down container
down:
	$(DOCKER_COMPOSE) down

# Add a rule to run the development server.
run:
	$(DJANGO_MANAGE) runserver

# Add a rule to deploy the server.
deploy: prepare migrate up run 
	