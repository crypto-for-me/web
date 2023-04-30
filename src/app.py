import os
import json
import flask
import logging

from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()
app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def index():
    target_time = datetime(2023, 7, 7, 0, 0, 0, tzinfo=timezone.utc).timestamp() * 1000
    formatted_time = '7/7/2023 0:00 AM'

    time_diff = target_time - datetime.now(timezone.utc).timestamp() * 1000
    days = int(time_diff / (1000 * 60 * 60 * 24))
    hours = int(time_diff / (1000 * 60 * 60)) % 24
    minutes = int(time_diff / (1000 * 60)) % 60
    seconds = int(time_diff / 1000) % 60

    return flask.render_template('index.html', formatted_time=formatted_time, days=days, hours=hours, minutes=minutes, seconds=seconds)

@app.route('/imprint')
def imprint():
    return flask.render_template('legal/imprint.html')

@app.route('/terms')
def terms():
    return flask.render_template('legal/terms.html')

@app.route('/privacy')
def privacy():
    return flask.render_template('legal/privacy.html')

@app.route('/gift-card-to-<currency>')
def gift_card_to_crypto(currency):
    with open('config/crypto_currencies.json', 'r') as f:
        currencies = json.load(f)

    currency = currencies.get(currency.upper(), None)

    with open('config/gift_cards.json', 'r') as f:
        cards = json.load(f)

    return flask.render_template('buy.html', crypto_currency=currency, cryptos=currencies, gift_cards=cards)

@app.context_processor
def inject_variables():
    VARS =  {
        'company': {}
    }

    # get all env variables as a dict
    for key, val in os.environ.items():
        if key.startswith('COMPANY_'):
            VARS['company'][key.split('_')[1].lower()] = val

    return VARS

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

app.run(host='0.0.0.0', port=2512, debug=True, use_evalex=False)
