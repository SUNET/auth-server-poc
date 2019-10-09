from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

app = Flask(__name__)
api = Api(app, prefix='/api/v1.0')

PEM_FILE = '/opt/auth-server-poc/cert/ec256-key-pair.pem'

app.config['JWT_PRIVATE_KEY'] = open(PEM_FILE).read()
app.config['JWT_PUBLIC_KEY'] = open(PEM_FILE).read()
app.config['JWT_ALGORITHM'] = 'ES256'
app.config['JWT_IDENTITY_CLAIM'] = 'sub'


class AuthApi(Resource):
    def post(self):
        access_token = create_access_token(identity=request.environ.get('REMOTE_USER'))
        return jsonify(access_token=access_token), 200


@app.route('/')
def index():
    return "<p>Username: {}</p><p>Auth type: {}</p>".format(request.environ.get('REMOTE_USER'),
                                                            request.environ.get('AUTH_TYPE'))


api.add_resource(AuthApi, '/auth')
