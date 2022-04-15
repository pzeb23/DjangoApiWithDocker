FROM python:3.10

ENV PYTHONBUFERRED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT