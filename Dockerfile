FROM python:3.10.6-buster

RUN mkdir /app
COPY . /app/
COPY pyproject.toml /app
COPY dataset1.txt /app
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main


EXPOSE 8000

ENV PYTHONPATH=/app

