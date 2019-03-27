#!/usr/bin/env bash
export PYTHONPATH=../src

echo ~~WITH TTY~~
python script.py

echo
echo ~~WITHOUT TTY~~
python script.py > script.log
cat script.log
