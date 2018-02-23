#!/bin/bash

hostname=$1

unset LC_ALL

rsync -avz ./ $hostname:raspi-grafana/ --exclude=.git --exclude=.vscode

ssh $hostname raspi-grafana/deploy.py
