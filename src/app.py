from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Environ: {}</p><p>Auth header: {}</p>".format(os.environ['REMOTE_USER'],
                                                             request.headers.get('Authorization'))
