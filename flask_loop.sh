# This is not the runner for nodes!
# This is the runner for the Flask server!

echo "Please enter your sudo password if asked."
sudo echo "Done. Server can start."

python -m pip install -r requirements.txt

while true
do
    echo · Started CFM ·
    python src/app.py
    echo · Stopped CFM ·
    sleep 3
done
