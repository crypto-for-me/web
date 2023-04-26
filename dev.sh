cd src

python -m pip install pipreqs
python -m pipreqs.pipreqs --force .
python -m pip install --upgrade -r requirements.txt
