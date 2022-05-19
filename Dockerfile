FROM python:buster as build

MAINTAINER Nubzzz "nubzzz@nubzzz.com

WORKDIR /app

COPY main.py /app/
COPY requirements.txt /app/
COPY wsgi.py /app/
COPY gunicorn.sh /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/app/gunicorn.sh"]
