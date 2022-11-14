FROM python:3.10-alpine

RUN apk update && apk add curl

RUN ["curl", "-fsSL", "https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.4.14/grpc_health_probe-linux-amd64", "-o", "/bin/grpc_health_probe"]
RUN ["chmod", "+x", "/bin/grpc_health_probe"]

ENV POETRY_VERSION=1.2.2
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "${PATH}:/root/.local/bin"
# The following supports numpy install
RUN apk --no-cache add musl-dev linux-headers g++

WORKDIR /src

COPY pyproject.toml poetry.lock ./
RUN ["poetry", "install", "--only", "main", "--no-root", "-v"]
COPY . .
RUN ["poetry", "install", "--only", "main", "-v"]

ENTRYPOINT ["poetry", "run"]
