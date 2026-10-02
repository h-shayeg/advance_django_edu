FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

COPY wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt

COPY ./core /app/

EXPOSE 8000