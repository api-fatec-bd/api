FROM python:3.8-slim-buster
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
        unixodbc-dev \
        unixodbc
COPY . .

