FROM python:3.12

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

WORKDIR /app

RUN pip3 install "poetry==1.8.3"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN poetry install --only main --no-interaction --no-root

COPY . /app/