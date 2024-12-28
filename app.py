#!/usr/bin/python

import time
import os
import json
import hvac
from flask import Flask
app = Flask(__name__)
# Initialize the Vault client
client = hvac.Client(url=os.getenv('VAULT_ADDR'))

# Authenticate using the token
client.token = os.getenv('VAULT_TOKEN')

# Read a secret
secret = client.secrets.kv.read_secret_version(path='hello-world')
START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return json.dumps(dict(secret), indent=4)
    #return "Hello World (Python)! (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
