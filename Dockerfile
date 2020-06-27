## Author Saurabh Saxena

FROM python:3.8.2-alpine3.11

LABEL maintainer = "saurabh.salcklife.io@gmail.com"

LABEL vendor = "Simba"

# set environment variables
ENV APP_HOME=/usr/src/app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# SET Python specific ENV vars
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true

RUN mkdir -p ${APP_HOME} /var/log/proto

# set work directory
WORKDIR ${APP_HOME}

COPY Pipfile.lock .
COPY Pipfile .

RUN pip install pipenv \
	&& pipenv install --deploy --system --ignore-pipfile

COPY src/ .
COPY scripts/ scripts/

EXPOSE 5000

ENTRYPOINT ./scripts/start.sh
