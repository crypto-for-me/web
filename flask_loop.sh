#!/bin/sh

$PYTHON_BIN -m pip install -r requirements.txt

while true
do
    echo "🚀 Starting CFM..."
    $PYTHON_BIN src/app.py
    echo "💥 CFM crashed. Restarting in 3 seconds..."
    sleep 3
done
