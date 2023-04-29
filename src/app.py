import json
import flask
import logging

app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/gift-card-to-<currency>')
def gift_card_to_crypto(currency):
    with open('config/crypto_currencies.json', 'r') as f:
        currencies = json.load(f)

    currency = currencies.get(currency.upper(), None)

    return flask.render_template('buy.html', crypto_currency=currency)

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

app.run(host='0.0.0.0', port=2512, debug=True, use_evalex=False)
