FROM python:3.11.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY ./commands/entrypoint.sh /usr/src/commands/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/commands/entrypoint.sh"]

