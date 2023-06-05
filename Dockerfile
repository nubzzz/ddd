FROM python:3.12.0b1-slim as build

MAINTAINER Nubzzz "nubzzz@nubzzz.com

ENV PYTHONGUNBUFFERED True

WORKDIR /app

COPY main.py /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT

CMD exec gunicorn main:app -w 1 --threads 3 -b :$PORT --timeout=120 --log-level=debug
