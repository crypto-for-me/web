import flask
import logging

import hidden_service

app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

app.run(host='0.0.0.0', port=2512, debug=True, use_evalex=False)
