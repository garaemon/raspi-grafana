#!/usr/bin/env python3

# script to setup grafana, telegraf and influxdb on raspberry pi

import sys
import subprocess
import os


def install_docker():
    try:
        # check command exists first
        subprocess.check_call(['command', '-v', 'docker'], shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_call(['curl -sSL https://get.docker.com/ | sh'], shell=True)

    subprocess.check_call(['sudo usermod -aG docker ${USER}'], shell=True)

    try:
        subprocess.check_call(['command', '-v', 'docker-compose'], shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_call(['sudo apt-get install docker-compose --yes'], shell=True)


def install_docker_images():
    subprocess.check_call(['docker-compose', 'pull'], cwd=os.path.join(os.path.dirname(__file__)))


def run_docker():
    subprocess.check_call(
        ['docker-compose', 'up', '-d'], cwd=os.path.join(os.path.dirname(__file__)))


def main():
    install_docker()
    install_docker_images()
    run_docker()


if __name__ == '__main__':
    main()
