FROM python:3.11-slim

WORKDIR /app

COPY .env .env
COPY urlshortener_cli/src/ .
COPY urlshortener_cli/pyproject.toml /code/pyproject.toml

RUN pip install /code/. \
    && chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]