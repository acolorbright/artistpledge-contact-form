import os
import requests

from flask import Flask, request, redirect

app = Flask(__name__)

MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
SITE_ADDRESS = os.environ['SITE_ADDRESS']
TO_NAME = os.environ['USER_NAME']
TO_EMAIL = os.environ['USER_EMAIL']


@app.route('/')
def index():
    return redirect(SITE_ADDRESS)


@app.route('/send', methods=['POST'])
def send_simple_message():
    response = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
        auth=('api', MAILGUN_API_KEY),
        data={
            'from': '{0} <{1}>'.format(request.form['name'], request.form['email']),
            'to': '{0} <{1}>'.format(TO_NAME, TO_EMAIL),
            'subject': 'Message from {}'.format(request.form['name']),
            'text': request.form['message'],
        }
    )
    return redirect(SITE_ADDRESS)


@app.errorhandler(500)
def error(e):
    return ('Sorry, something went wrong! %s - %s' % (e.__class__, e), 500)
