FROM python:3.11-alpine3.18
ARG RUN_ENV="development"

RUN apk add git

ENV RUN_ENV=${RUN_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1

# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /workspace/libreoffice_python
COPY ./pyproject.toml ./poetry.lock ./poetry.toml ./

# Project initialization:
# poetry config virtualenvs.create false
RUN poetry install $(test "$RUN_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-root

USER root
ENV HOME /root

WORKDIR /workspace/libreoffice_python

RUN if [ x"$GIT_AUTHOR_NAME" != "x" ]; then git config --global user.name "$GIT_AUTHOR_NAME" || true; fi \
    && if [ x"$GIT_AUTHOR_EMAIL" != "x" ]; then git config --global user.email $GIT_AUTHOR_EMAIL || true; fi


# WORKDIR $HOME

ENV VIRTUAL_ENV=/workspace/libreoffice_python/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# COPY ./.devcontainer/custom_bash.txt ./.bashrc_custom

ARG WD=/workspace/libreoffice_python/.venv/lib/python$PY_VER/site-packages

WORKDIR ${WD}

RUN ln -s /usr/lib/python3/dist-packages/uno.py uno.py \
    && ln -s /usr/lib/python3/dist-packages/unohelper.py unohelper.py \
    && echo "/workspace/libreoffice_python" >> ooo_dev_tools.pth