FROM python:3.8

RUN mkdir /app
RUN mkdir /app/static
COPY requirements.txt /app/.
WORKDIR /app
RUN apt-get update && apt install curl postgresql-client-11 postgresql-client-common -y
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
