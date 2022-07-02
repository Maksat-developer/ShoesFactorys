FROM python:3.10.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBYFFERED 1

WORKDIR /ShoesFactory


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
