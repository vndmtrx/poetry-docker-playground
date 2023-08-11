# Dockerfile
# Utiliza build multi-stage, o que requer Docker em versão 17.05 or posterior
# Veja em https://docs.docker.com/develop/develop-images/multistage-build/

#####################################################################
# Criação de uma imagem base com variáveis de ambiente compartilhadas
FROM python:3.11.4-slim-bookworm AS python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
    
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


######################################################
# Imagem builder-base usada para gerar as dependências
FROM python-base AS builder-base
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*

# Instalação do Poetry - respeita $POETRY_VERSION e $POETRY_HOME
ENV POETRY_VERSION=1.5.1
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} && \
    chmod a+x /opt/poetry/bin/poetry

# Aqui copiamos os requerimentos do projeto para gerar cache
# e instalamos apenas as dependências de cache usando o poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml .
RUN sed -e '/^packages/s/^/#/' -i pyproject.toml && poetry install --only main


#############################################################
# Imagem de desenvolvimento que instala todas as dependências
# pode ser usada para desenvolver código.
# por exemplo, usando docker-compose para montar a pasta local em /app
FROM python-base as dev
ENV FASTAPI_ENV=dev

# Copia o poetry e o venv para a imagem
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copia o entrypoint para conectar ao venv
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# O venv já possui as dependências de execução instaladas
WORKDIR $PYSETUP_PATH
COPY . .
RUN poetry install

EXPOSE 8000
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=8000", "hello_fastapi.main:app"]


#################################################################
# Imagem de produção, que usa uma instalação limpa do python-base
# e copia somente as dependências de execução que foram criadas em
# builder-base
FROM python-base AS prod
ENV FASTAPI_ENV=prod

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY gunicorn_conf.py /gunicorn_conf.py

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN groupadd -g 1500 poetry && useradd -m -u 1500 -g poetry poetry

COPY --chown=poetry:poetry ./hello_fastapi /hello_fastapi
USER poetry
WORKDIR /hello_fastapi

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--config /gunicorn_conf.py", "main:app"]
