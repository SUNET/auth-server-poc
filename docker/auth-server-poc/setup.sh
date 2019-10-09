#!/bin/bash

set -e
set -x

export DEBIAN_FRONTEND noninteractive

/bin/sed -i s/deb.debian.org/ftp.se.debian.org/g /etc/apt/sources.list

apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install -y \
      git \
      python3-venv \
      python3-pip \
      python3-yaml \
      iputils-ping \
      procps \
      bind9-host \
      netcat-openbsd \
      net-tools \
      curl \
      netcat \
      nginx \
      supervisor \
      libssl-dev \
    && apt-get clean

pip3 install uwsgi

# Start venv
python3 -m venv /opt/auth-server-poc/venv
cd /opt/auth-server-poc/venv/
source bin/activate

/opt/auth-server-poc/venv/bin/pip install -U pip

# Fetch the code and install dependencies
git clone https://github.com/SUNET/auth-server-poc.git
cd auth-server-poc/
python3 -m pip install -r requirements.txt

# Temporary for testing new branch
#cd /opt/cnaas/venv/cnaas-nms/
#git remote update
#git fetch
#git checkout --track origin/feature.websocket
#python3 -m pip install -r requirements.txt

#rm -rf /var/lib/apt/lists/*


