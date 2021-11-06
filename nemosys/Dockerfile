FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /nemosys
COPY requirements.txt /nemosys/
RUN apt-get update && apt-get install -y --no-install-recommends \
        unixodbc-dev \
        unixodbc
RUN pip3 install -r requirements.txt
COPY . /nemosys/