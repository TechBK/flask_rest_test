from flask import g, request
from flask_httpauth import HTTPTokenAuth
from notes_app_api import app, db, api
import hashlib
import jwt
from bson import json_util
import datetime
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

token_auth = HTTPTokenAuth()


def jwt_decode(jwt_payload):
    """

    :param jwt_payload:
    :return: User Object
    """
    user = jwt.decode(jwt_payload,
                      app.config.get('SECRET_KEY', 'TechBK_PRO')
                      )['user']
    return json_util.loads(user)


def jwt_encode(user):
    """

    :param user: UserObject
    :return:
    """
    return jwt.encode(
        {
            'user': json_util.dumps(user),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)
        },
        app.config.get('SECRET_KEY', 'TechBK_PRO'),
        algorithm='HS256'
    )


def hash_pass(password):
    # used to hash the password similar to how MySQL hashes passwords with the password() function.
    hash_password = hashlib.sha1(password.encode('utf-8')).digest()
    hash_password = hashlib.sha1(hash_password).hexdigest()
    hash_password = '*' + hash_password.upper()
    return hash_password


def do_token(login=None, password=None):
    # session = yield from get_session(request)
    # assert (session.get('user') is None), Exception('Need Logout before!')
    assert login, ValueError('None is allowed as login value')
    assert password, ValueError('None is not allowed as password value')
    user = db.users.find_one({'login': login})  # ,{'login': 1, '_id': 1, 'password': 1})
    assert user, ValueError('%s is not exist' % login)
    hash_password = hash_pass(password)
    if user['password'] != hash_password:
        raise Exception('Password is incorrect!')

    # session['user'] = json_util.dumps(user)
    user.pop('password', None)
    token = jwt_encode(user)

    return user, token


def do_signup(login=None, password1=None, password2=None):
    """
    do sign up.
    :param login:
    :param password1:
    :param password2:
    :return: user
    """
    assert login, 'Require Username'
    assert password1, 'Require Password'
    assert password2, 'Require Confirm Password'
    assert password1 == password2, 'Require Password'

    data = {'login': login.lower(), 'password': hash_pass(password1)}
    _id = db.users.insert(data)
    user = db.users.find_one({'_id': _id}, {'_id': 1, 'login': 1})
    return user


# @token_auth.error_handler
# def unauthorized_error():
#     raise Exception('Please authenticate to get your token.')

@token_auth.verify_token
def verify_token(token):
    if not token:
        return False
    try:
        user = jwt_decode(token)
    except jwt.ExpiredSignatureError:
        return False
    except Exception as e:
        raise e
    g.user = user
    return True


@api.resource('/token/')
class TokenApi(Resource):
    # @token_auth.login_required
    # def post(self):
    #     # user = g.user
    #     # assert user, ValueError('Code sai roi')
    #
    #     token = jwt_encode(user)
    #
    #     # user.pop('_id', None)
    #     return {'token': token}

    @token_auth.login_required
    def post(self):
        try:
            data = request.get_json()
        except BadRequest:
            raise Exception('Json is bad')
        data['login'] = data['login'].lower()
        user, token = do_token(**data)
        return {"user": user, 'token': token.decode('ascii')}, 200
