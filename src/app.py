import os
import json
import flask
import logging

from dotenv import load_dotenv

load_dotenv()
app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def index():
    return flask.render_template('index.html')

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
