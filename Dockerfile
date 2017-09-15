FROM phusion/baseimage:0.9.20
MAINTAINER Alli S. <none@none.com>

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && \
    apt-get install -y tar git vim nano wget net-tools build-essential \
        python2.7 python-pip jq && pip install requests argparse

RUN mkdir -p /opt/beyondverbal/ && \
    mkdir -p /opt/scripts/

COPY beyondverbal/* /opt/beyondverbal/
RUN chmod a+x /opt/beyondverbal/*

RUN mkdir -p /opt/input && \
    mkdir -p /opt/output && \
    chmod 777 /opt/input && \
    chmod 777 /opt/output

COPY docker/service /etc/service
RUN chmod a+x /etc/service/**/run

CMD ["/sbin/my_init"]
