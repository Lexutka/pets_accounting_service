FROM python:3.10.9-alpine

WORKDIR /usr/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.2.1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install --upgrade pip setuptools wheel && pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /usr/app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
ENV PYTHONPATH='/usr/app/'
COPY . /usr/app/
