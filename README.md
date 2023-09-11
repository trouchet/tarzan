# ![tarzan_title](https://github.com/trouchet/tarzan/blob/133557f070ecd8c2bdc3ab0eadf0de4639000e54/static/images/tarzan_tiny)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)
[![codecov](https://codecov.io/gh/trouchet/tarzan/graph/badge.svg?token=GSYO6WIEMD)](https://codecov.io/gh/trouchet/tarzan)

A Django app with routes and logging.

# How to operate

Run the commands below on `tarzan` root path:

### Prepare

- **What**: prepare environment for `poetry` usage:
- **How**: `make prepare`

**Remark**: Make sure to always have the environment activated with command above. It runs the target `env`, which generates the project's environment. Commands below require activated environment.

### Clean

- **What**: clean unnecessary asset files:
- **How**: `make clean`

### Run migrations

- **What**: Run migrations:
- **How**: `make migrate`

### Create admin user

- **What**: create superuser:
- **How**: `make sudo`

### Docker compose up

- **What**: build container image and host locally:
- **How**: `make up`

### List containers

- **What**: list containers, among them, `tarzan-box` and `tarzan-memory`:
- **How**: `make ps`

### Docker compose down

- **What**: bring container image down
- **How**: `make down`

### Run

- **What**: run the application:
- **How**: `make deploy`

### Deploy

- **What**: perform actions `build`, `up`, `migrate`, `sudo` and `run`:
- **How**: `make start`
