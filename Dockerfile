FROM python:3.13-slim

ENV POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

RUN mkdir -p /app/media /app/staticfiles

ENV CELERY_BROKER_URL="redis://redis:6379"
ENV CELERY_BACKEND="redis://redis:6379"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]