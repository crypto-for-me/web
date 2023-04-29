#!/bin/sh

PYTHON_BIN="/stuff/pypy3.9-v7.3.11-linux64/bin/pypy3.9"
export PYTHON_BIN
echo "PYTHON_BIN=$PYTHON_BIN"

./dev.sh
./run.sh