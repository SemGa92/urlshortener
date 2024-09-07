FROM python:3.11-slim

WORKDIR /app

COPY ./src/ .
COPY ./pyproject.toml /code/pyproject.toml

RUN pip install /code/. \
    && chmod +x entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]