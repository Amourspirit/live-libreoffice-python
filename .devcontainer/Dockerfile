ARG PY_VER=3.11
FROM python:$PY_VER-alpine3.18
ARG RUN_ENV="development"

USER root

RUN apk update \
    && apk add --no-cache git \
    openssh

ARG HOME=/root
# https://unix.stackexchange.com/questions/176027/ash-profile-configuration-file
COPY ./.devcontainer/rc.txt $HOME/.ashrc

ENV HOME=$HOME \
    RUN_ENV=${RUN_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1 \
    ENV=$HOME/.ashrc

# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /workspace/libreoffice_python
COPY ./pyproject.toml ./poetry.lock ./poetry.toml ./

# Project initialization:
# poetry config virtualenvs.create false
RUN poetry install $(test "$RUN_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-root

WORKDIR /workspace/libreoffice_python


# When in Github codespaces `CODESPACES=true` is set, so we can use that to add git shortcuts.
RUN if [ x"$GIT_AUTHOR_NAME" != "x" ]; then git config --global user.name "$GIT_AUTHOR_NAME" || true; fi \
    && if [ x"$GIT_AUTHOR_EMAIL" != "x" ]; then git config --global user.email $GIT_AUTHOR_EMAIL || true; fi \
    && if [ "$CODESPACES" == "true" ]; then git config --global alias.co checkout \
    && git config --global alias.br branch \
    && git config --global alias.ci commit \
    && git config --global alias.s "status -s" \
    && git config --global alias.type "cat-file -t" \
    && git config --global alias.dump "cat-file -p"; fi

ENV VIRTUAL_ENV=/workspace/libreoffice_python/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# it is not possible to set the build environment vars.
# To get a var to persit in this manor an entry point script would need to be implemented.
# The solution is to create the environment and use it all in the same command.
# See: https://forums.docker.com/t/how-do-i-send-runs-output-to-env-in-dockerfile/16106/2
RUN MY_PY_VER=$(python -c "import sys; major, minor = sys.version_info[:2]; print(f'{major}.{minor}');" ) \
    && echo $MY_PY_VER \
    && echo "/workspace/libreoffice_python" >> "/workspace/libreoffice_python/.venv/lib/python$MY_PY_VER/site-packages/ooo_dev_tools.pth"

# UNO version
# RUN ln -s /usr/lib/python3/dist-packages/uno.py uno.py \
#     && ln -s /usr/lib/python3/dist-packages/unohelper.py unohelper.py \
#     && echo "/workspace/libreoffice_python" >> ooo_dev_tools.pth

# RUN echo "/workspace/libreoffice_python" >> ooo_dev_tools.pth
WORKDIR /workspace/libreoffice_python
