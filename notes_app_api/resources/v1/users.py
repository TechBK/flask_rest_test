from flask.ext.restful import Resource
from notes_app_api import api, db
from flask import request
from werkzeug.exceptions import BadRequest
from notes_app_api import auth

SECRET = 'techbk_pro'


@api.resource('/users/<string:login>/', endpoint='user')
class UserAPI(Resource):
    def get(self, login):
        login = login.lower()
        user = db.users.find_one_or_404({'login': login}, {'password': 0})
        return user, 200

    @auth.token_auth.login_required
    def put(self, login):
        login = login.lower()
        try:
            data = request.get_json()
        except BadRequest:
            raise Exception('Json is bad')
        data.pop('_id', None)
        data.pop('login', None)
        data.pop('password', None)
        result = db.users.update({'login': login}, {'$set': data})
        user = db.users.find_one({'login': login}, {'password': 0})
        return user, 201

    def delete(self, id):
        pass


@api.resource('/users/', endpoint='users')
class UsersAPI(Resource):
    def get(self):
        users = db.users.find({}, {'password': 0})
        return users, 200

    def post(self):

        try:
            data = request.get_json()
        except BadRequest:
            raise Exception('Json is bad')
        user = auth.do_signup(**data)

        return user
