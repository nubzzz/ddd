FROM python:buster as build

MAINTAINER Nubzzz "nubzzz@nubzzz.com

WORKDIR /app

COPY main.py main.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["main.py"]
