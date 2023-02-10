#!/bin/bash

pip --version

mkdir local_lib
pip install --upgrade --force-reinstall path.py -t ./local_lib > ./file.log

python3 my_program.py