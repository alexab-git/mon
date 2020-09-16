#!/usr/bin/env bash

cd /tmp
#wget https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.40.1/victoria-metrics-v1.40.1.tar.gz
#tar -xf /tmp/victoria-metrics-v1.40.1.tar.gz -C /usr/local/bin/
cd -
mkdir /run/victoriametrics /var/lib/victoria-metrics-data
cp ./victoriametrics.service /etc/systemd/system/victoriametrics.service

