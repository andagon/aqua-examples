FROM docker.io/python:slim

RUN apt-get update \
    && apt-get install firefox-esr -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home vscode

USER vscode

RUN python -m pip install --upgrade pip \
    && python -m pip install --user pipx \
    && python -m pipx install poetry

WORKDIR /home/vscode