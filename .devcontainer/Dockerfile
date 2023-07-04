ARG LO_VERSION
FROM linuxserver/libreoffice:${LO_VERSION}

ARG CODE_PORT=2002
ARG HOME=/root

# Had Error: Compilation error in psutil/_psutil_linux
# See Github: https://github.com/giampaolo/psutil/issues/664
RUN apk update \
    && apk add --no-cache htop \
    linux-headers \
    libc-dev \
    gcc \
    python3-dev \
    git \
    openssh \
    py-pip

RUN sed -i "s/libreoffice/soffice --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /defaults/autostart \
    && sed -i "s/--base/--base --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/base.desktop \
    && sed -i "s/--calc/--calc --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/calc.desktop \
    && sed -i "s/--draw/--draw --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/draw.desktop \
    && sed -i "s/--impress/--impress --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/impress.desktop \
    && sed -i "s/--math/--math --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/math.desktop \
    && sed -i "s/--writer/--writer --accept=\"socket,host=localhost,port=${CODE_PORT},tcpNoDelay=1;urp;StarOffice.ServiceManager\"/g" /usr/lib/libreoffice/share/xdg/writer.desktop

# Codespaces mounts its own /tmp directory, so we need to create a new one
COPY ./.devcontainer/res $HOME/.tmp/res
COPY ./.devcontainer/res $HOME/.tmp/res
COPY ./.devcontainer/root/rc.txt $HOME/.ashrc


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



# Many of these environment variable are required for python and LibreOffice imports to work correctly.
# For instance without proper environment vars: from com.sun.star.frame import XComponentLoader # results in error
# many of these values can be gotten by opening APSO console in running isntance of LinuxServer LibreOffice and
# import os
# os.environ
# See Also: https://uucode.com/blog/2013/01/09/solved-createinstancewithcontext-binary-urp-bridge-disposed-during-call/
# Note: not all os's need extra LibreOffice Environment Vars, I did not have to do this for Ubuntu
ENV PATH="/usr/lib/libreoffice/program:$PATH" \
    URE_BOOTSTRAP="file:///usr/lib/libreoffice/program/fundamentalrc" \
    PYTHONPATH="/usr/lib/libreoffice/program/../program:$PYTHONPATH" \
    UNO_PATH="/usr/lib/libreoffice/program" \
    LD_LIBRARY_PATH="/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/client:/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/server:/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/native_threads:/usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64"

RUN if [ x"$GIT_AUTHOR_NAME" != "x" ]; then git config --global user.name "$GIT_AUTHOR_NAME" || true; fi \
    && if [ x"$GIT_AUTHOR_EMAIL" != "x" ]; then git config --global user.email $GIT_AUTHOR_EMAIL || true; fi

# install requirements.txt using pip
# don't need pip so add and remove it to keep image size smaller
RUN  /usr/bin/pip install "poetry==$POETRY_VERSION" \
    && if [ -f "$HOME/.tmp/res/req/requirements.txt" ]; then \
    /usr/bin/pip install --no-cache-dir -r "$HOME/.tmp/res/req/requirements.txt"; fi

WORKDIR /workspace/libreoffice_python_app
COPY ./pyproject.toml ./poetry.lock ./poetry.toml ./
RUN poetry install $(test "$RUN_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-root

RUN MY_PY_VER=$(python -c "import sys; major, minor = sys.version_info[:2]; print(f'{major}.{minor}');" ) \
    && echo $MY_PY_VER \
    && echo "/workspace/libreoffice_python_app" >> "/workspace/libreoffice_python_app/.venv/lib/python$MY_PY_VER/site-packages/ooo_dev_tools.pth" \
    && echo "/usr/lib/libreoffice/program" >> "/workspace/libreoffice_python_app/.venv/lib/python$MY_PY_VER/site-packages/libreoffice_program.pth"


WORKDIR /workspace/libreoffice_python_app

# EXPOSE $CODE_PORT
COPY ./.devcontainer/root/defaults /defaults
COPY ./.devcontainer/startup.sh /usr/local/bin/startup.sh

# Moved extension install to to here 
RUN chmod -R +x "$HOME/.tmp/res/scripts" \
    && mv "$HOME/.tmp/res/scripts/unlock.sh" "/usr/local/bin/unlock" \
    && chmod +x "/usr/local/bin/unlock" \
    && chmod +x "/defaults/autostart" \
    && mkdir -p "$HOME/.config/libreoffice/4/user/" \
    && mv "$HOME/.tmp/res/defaults/registrymodifications.xcu" "$HOME/.config/libreoffice/4/user/registrymodifications.xcu" \
    && mkdir -p "/usr/lib/libreoffice/share/extensions" \
    # && /tmp/res/scripts/ext.sh \
    && chmod +x "/usr/local/bin/startup.sh" \
    && mv "$HOME/.tmp/res/scripts/reload.sh" "/usr/local/bin/reload" \
    && chmod +x "/usr/local/bin/reload"



# ENTRYPOINT ["/usr/local/bin/startup.sh"]

