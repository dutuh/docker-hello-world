FROM python:3.8.6-slim-buster

WORKDIR /app

COPY src .

RUN pip install -r requirements.txt


