#!/bin/sh
echo "💠 Installing requirements..."

cd src
$PYTHON_BIN -m ensurepip # installs pip
$PYTHON_BIN -m pip install pipreqs # installs pipreqs
$PYTHON_BIN -m pipreqs.pipreqs --force . # generates requirements.txt
$PYTHON_BIN -m pip install --upgrade -r requirements.txt # installs or updates requirements
