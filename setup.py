#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="huobi-client",
    version="0.1",
    packages=find_packages(),
    install_requires=['requests', 'apscheduler', 'websocket', 'urllib3']
)
