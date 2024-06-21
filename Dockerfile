FROM python:3.11.5-slim-bookworm
WORKDIR /app

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.4.2 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . .
