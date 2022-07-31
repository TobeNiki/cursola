FROM python:3.7.13-slim

WORKDIR $HOME/usr/

ENV PYTHONPATH="/usr:$PYTHONPATH"
ENV TRANSFORMERS_OFFLINE=1

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN apt-get install -y \
    git \ 
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt $HOME/usr/

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

WORKDIR $HOME/usr/app

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000