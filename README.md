# ![tarzan_title](https://github.com/trouchet/tarzan/blob/133557f070ecd8c2bdc3ab0eadf0de4639000e54/static/images/tarzan_tiny)

A Django app with routes and logging.

# How to operate

Run the commands below on `tarzan` root path:

### Prepare
  
  - What: prepare environment for `poetry` usage:
  
  ```
  make prepare
  ```

### Clean

  - What: clean unnecessary asset files:

  ```
  make clean
  ```

### Run migrations

  - What: Run migrations:

  ```
  make migrate
  ```

### Create admin user

  - What: create superuser:

  ```
  make sudo
  ```

### Docker compose up

  - What: build container image and host locally:
  
  ```
  make up
  ```

### List containers 

  - What: list containers, among them, `tarzan-box` and `tarzan-memory`:
  
  ```
  make ps
  ```

### Docker compose down

  - What: bring container image down

  ```
  make down
  ```

### Run

  - What: run the application:

  ```
  make start
  ```

### Deploy

  - What: perform actions `prepare`, `build`, `up`, `migrate`, `sudo` and `run`:

  ```
  make start
  ```
