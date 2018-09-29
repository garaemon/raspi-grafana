FROM resin/rpi-raspbian:stretch

MAINTAINER garaemon <garaemon@gmail.com>
# Based on https://github.com/hypriot/rpi-influxdb

RUN curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - && \
    apt-get update && apt-get install -y apt-transport-https && \
    echo "deb https://repos.influxdata.com/debian stretch stable" | tee /etc/apt/sources.list.d/influxdb.list && \
    apt-get update && apt-get install -y influxdb && \
    apt-get remove --auto-remove -y apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

COPY influxdb.conf /etc/influxdb/influxdb.conf

ENV PRE_CREATE_DB **None**

# HTTP API
EXPOSE 8086

VOLUME ["/data"]

CMD ["/usr/bin/influxd"]
