FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./app /app

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1