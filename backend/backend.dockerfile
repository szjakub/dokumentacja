FROM python:3.7

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./app /app

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]