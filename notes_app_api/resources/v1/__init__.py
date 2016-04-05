from flask import request
from werkzeug.exceptions import BadRequest


class QueryMixin:
    @property
    def query(self):
        try:
            query = request.get_json()
            assert query is None or isinstance(query, dict), ValueError('Plzz give json')
        except BadRequest:
            query = {}
        return query
#
# class DataMixin:
#
#     @property
#     def data(self):