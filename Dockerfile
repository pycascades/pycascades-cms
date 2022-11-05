FROM python:3.10.4-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry

# Set working directory
WORKDIR /app

# Install the project requirements.
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry install --no-interaction --no-ansi

# HOTFIX FOR https://github.com/miracle2k/django-assets/issues/102
RUN sed -i "s/requires_system_checks = False/requires_system_checks = []/" \
    $(poetry show -v 2> /dev/null | head -n1 | cut -d ' ' -f 3)/lib/python3.10/site-packages/django_assets/management/commands/assets.py
