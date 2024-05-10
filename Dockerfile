FROM python:3.11-slim-buster

ENV DJANGO_SETTINGS_MODULE=wingz.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/app/wingz

WORKDIR /usr/app

RUN apt update; apt install -y git

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

CMD /bin/bash
