# Copyright 2021 Suresoft Technologies Inc.
# Licensed under the MIT
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y git bear perl gcc make rename wget
RUN apt install -y python3 python3-pip

# Install gcovr
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 100
RUN pip3 install gcovr

RUN git config --global user.email "yckim@suresofttech.com"
RUN git config --global user.name "Yeongcheol Kim"

RUN useradd --create-home --home-dir /home/workspace --shell /bin/bash defects4cpp
USER defects4cpp
WORKDIR /home/workspace
