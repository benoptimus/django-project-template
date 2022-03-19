FROM python:3.9-alpine

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT tru

WORKDIR /code

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    zlib \
    jpeg

# Installing temporary packages required for installing requirements.txt
RUN apk update && apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    zlib-dev \
    jpeg-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    docker-cli \
    mariadb-dev \
    --virtual .docker-compose-deps

# Update pip
RUN pip install --upgrade pip

RUN pip3 install docker-compose

COPY renew_certs.sh /etc/periodic/daily/renew_certs
RUN chmod +x /etc/periodic/daily/renew_certs

COPY . /code/
RUN pip install --no-cache-dir -r /code/requirements/base.txt
RUN pip install --no-cache-dir -r /code/requirements/local.txt

RUN chmod +x /code/wait-for-it.sh
# removing temporary packages from docker and removing cache

#TODO: uncomment on prod
#RUN apk del build-deps && apk del .docker-compose-deps

RUN find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip
