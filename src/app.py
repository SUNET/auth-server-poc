from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, JWTManager

app = Flask(__name__)
api = Api(app, prefix='/api/v1.0')
jwt = JWTManager(app)

PEM_PRIVATE = '/opt/auth-server-poc/cert/private.pem'
PEM_PUBLIC = '/opt/auth-server-poc/cert/public.pem'

app.config['JWT_PRIVATE_KEY'] = open(PEM_FILE).read()
app.config['JWT_PUBLIC_KEY'] = open(PEM_FILE).read()
app.config['JWT_ALGORITHM'] = 'ES256'
app.config['JWT_IDENTITY_CLAIM'] = 'sub'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False


class AuthApi(Resource):
    def post(self):
        access_token = create_access_token(identity=request.environ.get('REMOTE_USER'))
        return {'access_token': access_token}, 200


@app.route('/')
def index():
    return "<p>Username: {}</p><p>Auth type: {}</p>".format(request.environ.get('REMOTE_USER'),
                                                            request.environ.get('AUTH_TYPE'))


api.add_resource(AuthApi, '/auth')
