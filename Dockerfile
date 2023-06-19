FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

# Instalar las dependencias de Ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx supervisor

# Instalar Django
RUN pip3 install Django==3.2
#COPY . /code
WORKDIR /code
