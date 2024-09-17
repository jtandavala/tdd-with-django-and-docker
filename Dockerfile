FROM python:3.12-slim as base

# Install Poetry
ENV POETRY_HOME=/opt/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl gcc postgresql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
    && poetry --version

FROM base as builder

WORKDIR /app
COPY poetry.lock pyproject.toml ./

# Install both main and dev dependencies for development
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-interaction --no-root

FROM base as runner

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY . /app

RUN mkdir -p /db
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

FROM runner as development

WORKDIR /app
ENTRYPOINT [ "/app/entrypoint.sh" ]

FROM runner as production

# Set user and group
ARG user=django
ARG group=django
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}

# Switch to user
RUN chown -R ${uid}:${gid} /app
RUN chown -R ${uid}:${gid} /db

USER ${uid}:${gid}

WORKDIR /app/src
ENTRYPOINT [ "/app/entrypoint.sh" ]
