FROM python:3.9-slim

ENV PIP_NO_CACHE_DIR=True
ENV POETRY_VIRTUALENVS_CREATE=False

RUN apt-get update
RUN apt install -y \
gcc g++ python-dev librocksdb-dev build-essential \
libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev \
liblz4-dev libzstd-dev curl

RUN pip install -U \
    pip \
    setuptools \
    wheel \
    poetry

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev && \
    rm -rf ~/.cache/pypoetry/{cache,artifacts}

COPY ./telegram_sender ./telegram_sender

WORKDIR /telegram_sender

ENV HOST 0.0.0.0
ENV PORT 8001
CMD uvicorn main:app --host $HOST --port $PORT