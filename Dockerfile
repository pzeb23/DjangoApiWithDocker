FROM python:3.10

ENV PYTHONBUFERRED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt