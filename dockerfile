FROM python:3.14.7-slim AS builder

WORKDIR /build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       pkg-config \
       default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip wheel \
    --no-cache-dir\
    --wheel-dir /wheels\
    -r requirements.txt




FROM python:3.14.7-slim AS runtime

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home django

COPY --from=builder /wheels /wheels

RUN pip install \
    --no-cache-dir \
    /wheels/*

COPY --chown=django:django . .

USER django

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]