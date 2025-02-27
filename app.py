"""
A simple guestbook flask app.
"""
import flask
import os
from index import Index
from eth import Eth
from callback import Callback
from logout import Logout

app = flask.Flask(__name__)       # our Flask app
app.secret_key = os.urandom(24)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/callback',
                 view_func=Callback.as_view('callback'),
                 methods=["GET"])

app.add_url_rule('/eth',
                 view_func=Eth.as_view('eth'),
                 methods=['GET', 'POST'])

app.add_url_rule('/logout',
                 view_func=Logout.as_view('logout'),
                 methods=["GET"])

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=8000, debug=True)
