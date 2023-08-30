# ![tarzan_title](https://github.com/trouchet/tarzan/blob/133557f070ecd8c2bdc3ab0eadf0de4639000e54/static/images/tarzan_tiny)

A Django app with routes and logging.

# How to operate

Run the commands below on `tarzan` root path:

## Prepare
  
  - What: prepare environment for `poetry` usage:
  
  ```
  make prepare
  ```

## Clean

  - What: clean unnecessary asset files:

  ```
  make clean
  ```

## Create admin user

  - What: create superuser:

  ```
  make sudo
  ```

## Docker compose up

  - What: build container image and host locally:
  
  ```
  make up
  ```

## Docker compose down

  - What: bring container image down

  ```
  make down
  ```

## Run

  - What: run the application:

  ```
  make start
  ```

