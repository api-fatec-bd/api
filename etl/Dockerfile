FROM python:3.8-slim-buster
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
        unixodbc-dev \
        unixodbc
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip3 install pymongo
ENV PYTHONPATH="/app"
COPY . .