#!/bin/bash

python3 -m pip install virtualenv
python3 -m virtualenv --clear django_venv
source "./django_venv/bin/activate"
pip install -r requirements.txt