from flask import Flask, request
import time

app = Flask(__name__)

my_verify_token = 'Minhdz'

@app.route('/')
def home():
    return 'Home'

@app.route('/message-receive')
def mr():
    args = request.args
    mode = args.get('hub.mode')
    token = args.get('hub.verify_token')
    challenge = args.get('hub.challenge')
    if mode and token:
        if mode == 'subscribe' and token == my_verify_token:
            print('Webhook message')
            return challenge, 200

    else:
        return 'Not found', 404




app.run('0.0.0.0', port=8000)




