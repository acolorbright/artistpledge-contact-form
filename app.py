import os
import requests

from flask import Flask, request, redirect

app = Flask(__name__)

MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
SITE_ADDRESS = os.getenv('SITE_ADDRESS')
TO_NAME = os.getenv('TO_NAME')
TO_EMAIL = os.getenv('TO_EMAIL')
SUCCESS_PAGE = os.getenv('SUCCESS_PAGE')


@app.route('/')
def index():
    return redirect(SITE_ADDRESS)


@app.route('/send', methods=['POST'])
def send_simple_message():
    response = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN),
        auth=('api', MAILGUN_API_KEY),
        data={
            'from': '{0} <{1}>'.format(request.form.get('name'), request.form.get('email')),
            'to': '{0} <{1}>'.format(TO_NAME, TO_EMAIL),
            'subject': 'Artist Pledge contact request from {}'.format(request.form.get('name')),
            'text': '''
            From: {}
            Email: {}
            Phone Number: {}

            Interested in: {}
            Enquiring for: {}

            Subscribe to newsletter? {}

            Message:
            {}
            '''.format(
                request.form.get('name', '–'),
                request.form.get('email', '–'),
                request.form.get('phone', '–'),
                request.form.get('interested-in', '–'),
                request.form.get('enquiring-for', '–'),
                request.form.get('newsletter') == 'on' and 'Yes' or 'No',
                request.form.get('message', 'None given'),
            ),
        }
    )
    return redirect(SUCCESS_PAGE)


@app.errorhandler(500)
def error(e):
    return ('Sorry, something went wrong! %s - %s' % (e.__class__, e), 500)
