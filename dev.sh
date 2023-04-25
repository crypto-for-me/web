cd src

python -m pip install pipreqs
python -m pipreqs.pipreqs --force .
python -m pip install --upgrade -r requirements.txt

npx tailwindcss -i static/css/main.css -o static/css/output.css --watch
