from flask import Flask
from flask.ext.restful import Api
from flask.ext.pymongo import PyMongo
from notes_app_api.config import Config
from flask import make_response
from bson import json_util

app = Flask(__name__)
app.config.from_object(Config)
pymongo = PyMongo(app)
with app.app_context():
    db = pymongo.db

# DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)


# api.representations = DEFAULT_REPRESENTATIONS

@api.representation('application/json')
def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    :param obj:
    """
    resp = make_response(json_util.dumps(obj), code)
    resp.headers.extend(headers or {})

    return resp


from . import views
from .resources.v1 import users, notes
from . import auth
