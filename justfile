set dotenv-load := false

# Show all available recipes
default:
  @just --list --unsorted


# Build all (or specified) container(s)
build service="":
    docker-compose build {{ service }}

# Bring all Docker services up
up flags="":
    docker-compose up -d {{ flags }}

# Take all Docker services down
down flags="":
    docker-compose down {{ flags }}

# Recreate all volumes and containers from scratch
recreate:
    @just down
    rm db.sqlite3
    @just up "--force-recreate --build"

# Show logs of all, or named, Docker services
logs service="": up
    docker-compose logs -f {{ service }}

# Open a shell into the webserver container
shell: up
    docker-compose exec /bin/bash

# Run a given command using the webserver image
run *args:
    docker-compose run --rm app {{ args }}

# Migrate the database
migrate:
    @just run poetry run python manage.py migrate
