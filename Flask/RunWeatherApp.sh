#!/bin/bash

virtualenv venv -p python3
source ./venv/bin/activate
pip3 install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=run.py
