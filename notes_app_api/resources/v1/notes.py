from flask import request, g
from flask_restful import Resource
from notes_app_api import api, db
from notes_app_api.auth import token_auth as auth
from bson import ObjectId
from . import QueryMixin


@api.resource('/users/<string:login>/notes/')
class PublicNotesOfUserAPI(Resource, QueryMixin):
    def get(self, login):
        query = self.query
        if query:
            query.update({'users': {'$all': [login]},
                          'public': True})
        else:
            # query = {'users': {'$all': [login]}, 'public': True}
            query = {'users': {'$all': [login]}}

        return db.notes.find(query), 200


@api.resource('/notes/')
class NotesAPI(Resource, QueryMixin):
    decorators = [auth.login_required]

    def get(self):
        # try:
        #     query = request.get_json()
        #     assert isinstance(query, dict)
        # except BadRequest:
        #     query = {}
        query = self.query.update({'users': {'$all': [g.user['login']]}})

        return db.notes.find(query), 200

    def post(self):
        data = request.get_json()
        if not isinstance(data, list):
            data = [data]
        for note in data:
            if 'users' not in note:
                note['users'] = [g.user['login']]
            elif g.user['login'] not in note.get('user'):
                note['users'].append(g.user['login'])
        ids = db.notes.insert(data)
        if not isinstance(ids, list):
            ids = [ids]

        return db.notes.find({'_id': {'$in': ids}}), 200


@api.resource('/notes/<string:id>/')
class NoteUserAPI(Resource, QueryMixin):
    decorators = [auth.login_required]

    def get(self, _id):
        query = self.query.update({'users': {'$all': [g.user['login']]},
                                   '_id': ObjectId(_id)})
        return db.notes.find(query), 200

    def put(self, _id):
        pass


@api.resource('/tags/<string:tag>/')
class PublicNotesOfTagAPI(Resource, QueryMixin):
    def get(self, tag):
        query = self.query
        if query:
            query = self.query.update({'tags': {'$all': [tag]},
                                       'public': True})
        else:
            query = {'tags': {'$all': [tag]}, 'public': True}

        return db.notes.find(query), 200
