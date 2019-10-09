from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>Remote user: {}</span>".format(os.environ['REMOTE_USER'])
