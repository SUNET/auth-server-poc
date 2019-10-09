from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Username: {}</p><p>Auth type: {}</p>".format(request.environ.get('REMOTE_USER'),
                                                            request.environ.get('AUTH_TYPE'))

