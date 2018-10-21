FROM python:2.7

ENV TZ Europe/Paris

COPY requirements.txt /srv/
RUN pip install --requirement /srv/requirements.txt
# set timezone for logs
RUN apt-get update && \
    apt-get -y install --no-install-recommends tzdata && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure --frontend=noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY players.py /srv/

WORKDIR /srv

CMD python /srv/players.py
